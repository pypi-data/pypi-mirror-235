import logging
import json
import re
from datetime import datetime

from openai import ChatCompletion
from openai.error import (
    Timeout, APIConnectionError, APIError, ServiceUnavailableError,
    InvalidRequestError, AuthenticationError, RateLimitError
)
from pydantic import BaseModel
from typing import List, Optional

logger = logging.getLogger(__name__)


class UsageModel(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int


class FunctionModel(BaseModel):
    arguments: str
    name: str


class MessageModel(BaseModel):
    content: Optional[str] = ''
    function_call: Optional[FunctionModel]
    role: str


class ChoiceModel(BaseModel):
    finish_reason: str
    index: str
    message: MessageModel


class CompletionModel(BaseModel):
    id: str
    choices: List[ChoiceModel]
    created: int
    model: str
    object: Optional[str] = 'chat.completion'
    usage: UsageModel


class FakeOpenAIChatCompletion(ChatCompletion):
    """
    Emulates the class openai.ChatCompletion letting the tester write an answer,
    so that one can simulate all possible scenarios (hallucinations, exceptions, ...)
    """

    # Probability of calling a function
    call_function_prob = 0.8

    @classmethod
    def create(cls, **kwargs):

        timestamp = datetime.now().timestamp()
        tid = hash(timestamp)

        try:
            prompt = '\n'.join(
                [m['role'] + '❯ ' + m['content'] for m in kwargs['messages']]
            )
        except KeyError:
            prompt = ''

        # I'm just making the prompt colored to make it easier to read
        col_prompt = re.sub(
            'user❯',
            '\033[1m\033[92muser\033[0m❯',
            re.sub(
                'system❯',
                '\033[1m\033[91msystem\033[0m❯',
                re.sub(
                    'assistant❯',
                    '\033[1m\033[94msystem\033[0m❯',
                    prompt
                )
            )
        )
        print(
            f'\033[1mI got:\033[0m\n\n{col_prompt}\n\n'
        )
        # Here I allow the tester (myself) to write a ChatGPT answer
        reply = input('What should I reply? ')
        # To raise an exception just raise it as if it was python code
        if re.match('^raise', reply):
            raise eval(
                re.sub(r'^raise\s+', '', reply),
                {
                    'Timeout': Timeout,
                    'APIConnectionError': APIConnectionError,
                    'APIError': APIError,
                    'ServiceUnavailableError': ServiceUnavailableError,
                    'InvalidRequestError': InvalidRequestError,
                    'AuthenticationError': AuthenticationError,
                    'RateLimitError': RateLimitError
                }
            )

        response = CompletionModel(**{
            'id': f'chatcmpl-{tid}',
            'object': 'chat.completion',
            'created': int(timestamp),
            'model': 'gpt-3.5-turbo-0613',
            'choices': [{
                'index': 0,
                'message': {
                    'role': 'assistant',
                    'content': reply,
                },
                'finish_reason': 'something' if re.match('^bad stop$', reply) else 'stop'
            }],
            'usage': {
                'prompt_tokens': len(prompt),
                'completion_tokens': len(reply),
                'total_tokens': len(prompt) + len(reply)
            }
        })

        logger.info(json.dumps(
            {
                'all_arguments': kwargs,
                'response_given': response.dict(),
            },
            indent=4
        ))
        logger.info('\n\n.::END_LOG::.\n\n')

        return response
