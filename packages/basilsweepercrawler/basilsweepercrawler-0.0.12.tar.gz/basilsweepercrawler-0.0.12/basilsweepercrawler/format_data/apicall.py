"""
Module for making OpenAI API calls.
"""
import time
import os
from dataclasses import dataclass
from typing import Callable, Literal, Optional, List, Dict, Any
import logging

import openai
from openai import ChatCompletion
from openai.error import (
    Timeout, APIConnectionError, APIError, ServiceUnavailableError,
    InvalidRequestError, AuthenticationError, RateLimitError
)
import tiktoken

from basilsweepercrawler.format_data.exceptions import (
    AllFailedError, OpenAIBadStopError, OpenAITooManyTokensError, PostProcessorError
)


def _tokens(model: str, text: str) -> int:
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))


# Mapping {openai model: max context length}
_model_dict = {
    "gpt-4": 8192,
    "gpt-4-32k": 32768,
    "gpt-3.5-turbo": 4096,
    "gpt-3.5-turbo-16k": 16384,
    "gpt-3.5-turbo-0613": 4096,
    "gpt-3.5-turbo-16k-0613": 16384,
}


# Errors for which we allow to retry
RETRY_ERRORS = (
    Timeout,
    APIConnectionError,
    APIError,
    ServiceUnavailableError,
    OpenAIBadStopError,
    OpenAITooManyTokensError,
)

# Errors which we consider fatal
NO_RETRY_ERRORS = (
    InvalidRequestError,
    AuthenticationError,
    RateLimitError,
)

OpenAIModels = Literal[
    'gpt-4', 'gpt-4-32k', 'gpt-3.5-turbo', 'gpt-3.5-turbo-16k',
    'gpt-3.5-turbo-0613', 'gpt-3.5-turbo-16k-0613'
]


logger = logging.getLogger(__name__)


@dataclass
class RetryRule:
    """Rules dictating how to retry an API call"""
    max_retries: int = 3
    retry_wait: int = 10  # seconds
    retry_errors: tuple = RETRY_ERRORS  # retry if encountered these errors
    no_retry_errors: tuple = NO_RETRY_ERRORS  # do not retry if encountered these


class OpenAICall:
    """
    Interface for making API calls to OpenAI and automatically retrying
    in case of failure.

    Arguments
    ---------
    models : Optional[List[OpenAIModels]] = None
        List of models to use ordered by size
    model_params : Optional[dict] = None
        Optional parameters to the models
    openai_key : Optional[str]
        API key for OpenAI, if absent the key is taken from the environment variable $OPENAI_API_KEY
    extra_instructions : Optional[List[str]]
        System messages to prepend to the prompt
    postprocessor : Optional[Callable] = None
        A postprocessor on the output that takes text and raises PostProcessorException if fails
    retry : RetryRule
        Rule dictating how to retry upon failure
    """

    def __init__(
        self,
        # OpenAI parameters
        models: Optional[List[OpenAIModels]] = None,
        model_params: Optional[dict] = None,
        openai_key: Optional[str] = None,
        # instructions
        extra_instructions: Optional[List[str]] = None,
        postprocessor: Optional[Callable[[str], Any]] = None,
        # retry rules
        retry: RetryRule = RetryRule(),
    ):
        if openai_key is not None:
            openai.api_key = openai_key
        else:
            try:
                openai.api_key = os.environ["OPENAI_API_KEY"]
            except KeyError:
                logger.error('OpenAI API key not found in environment variable. Exiting')
                raise

        if models is None:
            models = ['gpt-3.5-turbo', 'gpt-4']
        self.models = models
        self.retry = retry
        if model_params is None:
            model_params = {}
        self.model_params = model_params
        if "temperature" not in model_params:
            model_params["temperature"] = 0

        self.system_messages = []
        if extra_instructions:
            self.system_messages.extend(extra_instructions)

        self.postprocessor = postprocessor

    def _raw_api_request(self, model: str, messages: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Make an OpenAPI request and return the raw response.
        """
        if os.environ['TESTING'] == 'YES':
            from basilsweepercrawler.format_data.test_utils import FakeOpenAIChatCompletion
            completion = FakeOpenAIChatCompletion.create(
                model=model,
                messages=messages,
                **self.model_params,
            )
        else:
            completion = ChatCompletion.create(
                model=model,
                messages=messages,
                **self.model_params,
            )
        try:
            choice = completion.choices[0]
        except IndexError:
            raise APIError('there was no choice in the ChatCompletion object')

        try:
            if choice.finish_reason != 'stop':
                raise OpenAIBadStopError(f'the finish reason was not stop but "{choice.finish_reason}"')
            return messages + [choice.message.dict()]
        except AttributeError as e:
            raise APIError(f'the attribute "{e}" was not found')

    def _api_request(self, content: str | List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Make an OpenAPI request, with retries and model upgrades.
        """
        attempts = 0
        model_index = 0
        model = self.models[model_index]

        if isinstance(content, str):
            messages = [
                {"role": "system", "content": msg}
                for msg in self.system_messages
            ] + [
                {"role": "user", "content": content},
            ]
        else:
            messages = content

        while True:
            try:
                # check this within retries, but before API call
                # so that we don't waste an API call but can still
                # upgrade models
                model = self.models[model_index]
                max_tokens = _model_dict[model]
                tokens = _tokens(model, str(content))
                if tokens > max_tokens:
                    logger.warning(
                        f"the content is {tokens} tokens, max for {model} is "
                        f"{max_tokens}"
                    )
                    raise OpenAITooManyTokensError(tokens)

                attempts += 1
                out = self._raw_api_request(
                    model=model,
                    messages=messages
                )
            except self.retry.retry_errors as e:
                if attempts < self.retry.max_retries + 1:
                    if isinstance(e, OpenAIBadStopError) or isinstance(e, OpenAITooManyTokensError):
                        if model_index < len(self.models) - 1:
                            # try next model
                            model_index += 1
                            model = self.models[model_index]
                            logger.warning(f'Error: {e.__repr__()}. Retrying with next model: {model}')
                            time.sleep(self.retry.retry_wait)
                            continue
                        else:
                            logger.error('Ran out of models to try')
                            raise AllFailedError('Ran out of models to try', AllFailedError.MAX_RETRIES)
                    else:
                        logger.warning(f'Error: {e.__repr__()}. Retrying with same model: {model}')
                        # try again with same model
                        time.sleep(self.retry.retry_wait)
                        continue
                else:
                    logger.error('Ran out of attempts')
                    raise AllFailedError('Ran out of attempts', AllFailedError.MAX_RETRIES)
            except self.retry.no_retry_errors as e:
                logger.error('Fatal error: ' + e.__repr__())
                raise AllFailedError(e.__repr__(), AllFailedError.FATAL_ERROR)
            else:
                return out

    def _apply_postprocessors(self, response: List[Dict[str, str]]) -> Any:
        """
        Apply postprocessors to a response and retry if they fail
        """
        if self.postprocessor:
            logger.info('Applying postprocessor')
            attempts = 0
            current_response = response

            while True:
                try:
                    attempts += 1
                    result = self.postprocessor(current_response[-1]['content'])
                except PostProcessorError as e:
                    new_message = {'role': 'user', 'content': e.retry_message()}
                    if attempts <= self.retry.max_retries:
                        new_request = current_response + [new_message]
                        current_response = self._api_request(new_request)
                    else:
                        logger.error('Ran out of attempts in postprocessor stage')
                        raise AllFailedError('Ran out of attempts in postprocessor stage', AllFailedError.MAX_RETRIES)
                else:
                    return result
        else:
            return response

    def request(self, content: str) -> Any:
        """
        Make an OpenAPI request, with retries and model upgrades, and
        postprocessing.

        Arguments
        --------
        content : str
            The text of the request

        Returns
        -------
        Any
            The output of the postprocessor if any, otherwise the response by ChatGPT

        Raises
        ------
        OpenAICall.AllFailedError
            If all retries fail or if there is a fatal error
        """
        return self._apply_postprocessors(self._api_request(content))
