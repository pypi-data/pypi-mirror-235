import json
from json import JSONDecodeError
import jsonschema
from jsonschema.exceptions import ValidationError, SchemaError
from jsonschema.validators import Draft201909Validator as Validator
import logging
from typing import Iterable, Any, Optional, Callable, List, Iterator, Hashable
from abc import ABC, abstractmethod
import datetime

from basilsweepercrawler.format_data.apicall import OpenAICall, PostProcessorError
from basilsweepercrawler.format_data.exceptions import AllFailedError
from searchdatamodels import Candidate, DescriptionModel, WorkExperience, EducationExperience

logger = logging.getLogger(__name__)


class CandidateSchema:
    _str = {'type': 'string'}

    @staticmethod
    def _array(arg):
        return {
            'type': 'array',
            'items': arg
        }

    work_exp_schema = {
        'type': 'object',
        'properties': {
            'Institution': _str,
            'InstitutionDescription': _str,
            'Specialization': _str,
            'SpecializationDescription': _str,
            'Start': {'type': 'string', 'format': 'date'},
            'End': {'type': 'string', 'format': 'date'},
        },
        'required': [],
        'additionalProperties': False
    }

    edu_exp_schema = {
        'type': 'object',
        'properties': work_exp_schema['properties'] | {
            'Degree': _str,
        },
        'required': [],
        'additionalProperties': False
    }

    contact_schema = {
        'type': 'object',
        'properties': {
            'Type': _str,
            'Value': _str,
        },
        'required': ['Value'],
        'additionalProperties': False
    }

    candidate_schema = {
        'type': 'object',
        'properties': {
            'Name': _str,
            'Location': _str,
            'Picture': _str,
            'Summary': _str,
            'Skills': _array(_str),
            'WorkExperienceList': _array(work_exp_schema),
            'EducationExperienceList': _array(edu_exp_schema),
            'ContactInfoList': _array(contact_schema),
            'Sources': _array(_str),
            'ProjectList': _array(_str),
        },
        'required': ['Name'],
        'additionalProperties': False
    }

    descriptions = {
        # We put only a selection of the tags since others may be already obvious to the LLM
        'Institution': 'the place where the experience was carried out',
        'Specialization': 'the role of the candidate in this specific experience',
        'Degree': 'the degree obtained (phd, bachelor, ...)',
        'Picture': "the url of the candidate's picture",
        'Type': 'the type of contact (phone, email, ...)',
        'Location': 'location formatted as "city, region, country", "city, state, country" or "city, country"',
        'Sources': 'urls of personal websites or social media pages',
    }


def all_keys(obj: dict) -> Iterator[Hashable]:
    """
    Given a possibly nested dict returns all keys that appear in the form of an iterator
    """
    for k, v in obj.items():
        yield k
        if isinstance(v, list):
            for o in v:
                if isinstance(o, dict):
                    for a in all_keys(o):
                        yield a
        elif isinstance(v, dict):
            for a in all_keys(v):
                yield a


class RawProfile(ABC):
    """
    Raw profile as provided by the scraper. This class possesses methods to return a Candidate instance

    Arguments
    ---------
    profile : dict | str
        Either a dict with the profile or a string representing the location of the file
    open_fn : Optional[Callable] = open
        The open function to be used (either the builtin open or a class that reads from S3)
    **kwargs : dict
        Additional options to pass to the OpenAICall instance
    """

    before_text = '\n\nText output:\n'
    before_list = '\n\nList output:\n'
    before_json = '\n\nJSON output:\n'
    before_schema = '\n\nSchema:\n'
    before_prompt = '\n\nText:\n'

    def __init__(self, profile: dict | str, open_fn: Optional[Callable] = open, **kwargs):
        if isinstance(profile, dict):
            self.profile = profile
        elif isinstance(profile, str):
            try:
                with open_fn(profile, 'r') as f:
                    self.profile = json.loads(f.read())
            except FileNotFoundError:
                logger.error('path provided is not a file')
                raise
            except JSONDecodeError:
                logger.error('file provided does not contain valid JSON')
                raise
        else:
            raise TypeError

        self.openai_kwargs = kwargs

    @property
    @abstractmethod
    def json_system_msgs(self):
        """System message to perform text-to-schema transformation"""
        pass

    @property
    @abstractmethod
    def text_system_msgs(self):
        """System message to perform text-to-text transformation"""
        pass

    @property
    @abstractmethod
    def list_system_msgs(self):
        """System message to perform text-to-list transformation"""
        pass

    @staticmethod
    def get_path(obj: dict, path: Iterable[str]) -> Any:
        """Addresses a dict via a JSON-like path, like get_path(d, ['a', 'b', 'c']) == d['a']['b']['c']"""
        start = obj
        for p in path:
            start = start[p]
        return start

    @staticmethod
    def validate_schema(schema: dict) -> Callable[[str], dict]:
        """
        Takes a string, tries to parse it into JSON, then returns the structured result

        Arguments
        ---------
        schema : dict
            Schema to validate it against

        Returns
        -------
        Callable[[str], dict]
            function taking input string to JSON which raises PostProcessorException
            if schema validation or JSON parsing fails
        """
        def f(string: str) -> dict:
            try:
                parsed = json.loads(string)
            except JSONDecodeError as e:
                raise PostProcessorError(
                    reason=e.msg + " (here: '" + string[e.pos-10: e.pos] + "')",
                    fix='to output valid JSON.' + RawProfile.before_json
                )
            else:
                try:
                    jsonschema.validate(parsed, schema, format_checker=Validator.FORMAT_CHECKER)
                except SchemaError as e:
                    logger.error(f'The schema given is not valid {e}')
                    raise
                except ValidationError as e:
                    if 'format' in e.schema_path:
                        correct_format = RawProfile.get_path(schema, e.schema_path)
                        if correct_format == 'date':
                            fix = 'to format dates as yyyy-mm-dd.'
                        else:
                            fix = f'to format as {correct_format}'
                    elif 'required' in e.schema_path:
                        fix = ('that the properties: ' +
                               ', '.join(RawProfile.get_path(schema, e.schema_path)) +
                               ' are required.')
                    elif 'type' in e.schema_path:
                        fix = f'that the required type is "{RawProfile.get_path(schema, e.schema_path)}".'
                    elif 'additionalProperties' in e.schema_path:
                        fix = f"to never add properties that weren't specified in the schema or to check your spelling."
                    else:
                        fix = 'to output JSON conformant to the schema.'
                    raise PostProcessorError(
                        reason=e.message + f' (in property {e.json_path})',
                        fix=fix + RawProfile.before_json
                    )
                else:
                    return parsed

        return f

    @staticmethod
    def validate_list() -> Callable[[str], list]:
        """
        Takes a string, tries to parse it into a list, then returns the list

        Returns
        -------
        Callable[[str], list]
            function taking input string to list which raises PostProcessorException
            if list parsing fails
        """
        def f(string: str) -> list:
            try:
                parsed = eval(string)
            except SyntaxError as e:
                raise PostProcessorError(
                    reason=e.msg,
                    fix='to output a valid list.' + RawProfile.before_list
                )
            except NameError as e:
                raise PostProcessorError(
                    reason=str(e),
                    fix='to quote all text like "this".' + RawProfile.before_list
                )
            else:
                if isinstance(parsed, list):
                    return parsed
                else:
                    raise PostProcessorError(
                        reason=f'the output is of type {type(parsed)} and not list',
                        fix='to return a list.' + RawProfile.before_list
                    )

        return f

    def text_to_schema(
            self,
            text: str,
            schema: dict,
            additional_msgs: Optional[List[str]] = None,
            include_descriptions: Optional[bool] = False,
    ) -> dict:
        """
        Takes a text and a JSON schema and prompts OpenAI to return JSON conforming that schema

        Arguments
        --------
        text : str
            Raw input text
        schema : dict
            Target JSON schema
        additional_msgs : Optional[List[str]]
            Optionally pass additional messages to OpenAI
        include_descriptions : Optional[bool] = False
            Includes the descriptions of the fields from the CandidateSchema.descriptions dict

        Returns
        -------
        dict
            Structured JSON data

        Raises
        ------
        OpeAICall.AllFailedError
            If the OpenAI call is not successful
        """
        if additional_msgs is None:
            additional_msgs = []

        if include_descriptions:
            descriptions = 'Keep in mind that:\n' + '; '.join([
                f'{field} contains {desc}'
                for field, desc in CandidateSchema.descriptions
                if field in all_keys(schema)
            ]) + '.'
            additional_msgs = [descriptions] + additional_msgs

        messages = self.json_system_msgs + additional_msgs
        schema_text = (
                self.before_schema +
                json.dumps(schema) +
                self.before_prompt
        )
        validator = self.validate_schema(schema)
        chat = OpenAICall(
            postprocessor=validator,
            extra_instructions=messages,
            **self.openai_kwargs
        )
        try:
            result = chat.request(schema_text + text + self.before_json)
        except AllFailedError:
            logger.error('Unable to return a correctly formatted JSON; propagating exception')
            raise
        else:
            return result

    def text_to_text(self, text: str, additional_msgs: Optional[List[str]] = None) -> str:
        """
        Takes a text and prompts OpenAI to return text formatted properly

        Arguments
        --------
        text : str
            Raw input text
        additional_msgs : Optional[List[str]]
            Optionally pass additional messages to OpenAI

        Returns
        -------
        str
            Properly formatted text

        Raises
        ------
        OpeAICall.AllFailedError
            If the OpenAI call is not successful

        """
        if additional_msgs is None:
            additional_msgs = []

        messages = self.text_system_msgs + additional_msgs
        chat = OpenAICall(
            extra_instructions=messages,
            **self.openai_kwargs
        )
        try:
            result = chat.request(self.before_prompt + text + self.before_text)
        except AllFailedError:
            logger.error('Unable to return a correctly formatted text; propagating exception')
            raise
        else:
            return result

    def text_to_list(self, text: str, additional_msgs: Optional[List[str]] = None) -> List[str]:
        """
        Takes a text and prompts OpenAI to return a list of strings formatted properly

        Arguments
        --------
        text : str
            Raw input text
        additional_msgs : Optional[List[str]]
            Optionally pass additional messages to OpenAI

        Returns
        -------
        List[str]
            Properly formatted list

        Raises
        ------
        OpeAICall.AllFailedError
            If the OpenAI call is not successful
        """
        if additional_msgs is None:
            additional_msgs = []

        messages = self.list_system_msgs + additional_msgs
        chat = OpenAICall(
            postprocessor=self.validate_list(),
            extra_instructions=messages,
            **self.openai_kwargs
        )
        try:
            result = chat.request(self.before_prompt + text + self.before_list)
        except AllFailedError:
            logger.error('Unable to return a correctly formatted list; propagating exception')
            raise
        else:
            return result

    @abstractmethod
    def make_candidate(self) -> Candidate:
        """
        Returns a Candidate instance corresponding to the profile scraped

        Returns
        -------
        Candidate
            an instance of the Candidate data model
        """
        pass

    @staticmethod
    def make_description_model(text: str) -> DescriptionModel:
        """Make a DescriptionModel from text"""
        return DescriptionModel(Text=text)

    @staticmethod
    def make_date(date: str) -> datetime.date | None:
        """Make a date from a string"""
        if date:
            try:
                return datetime.date.fromisoformat(date)
            except ValueError:
                logger.warning("Somehow a date that wasn't correctly formatted passed through the validator")
                return None
        else:
            return None

    @staticmethod
    def make_work_experience(model: dict) -> WorkExperience:
        """Make a WorkExperience from its fields as plain strings"""
        return WorkExperience(
            Institution=model.get('Institution', ''),
            InstitutionDescription=RawProfile.make_description_model(model.get('InstitutionDescription', '')),
            Specialization=model.get('Specialization', ''),
            SpecializationDescription=RawProfile.make_description_model(model.get('SpecializationDescription', '')),
            Start=RawProfile.make_date(model.get('Start')),
            End=RawProfile.make_date(model.get('End')),
        )

    @staticmethod
    def make_education_experience(model: dict) -> EducationExperience:
        """Make an EducationExperience from its fields as plain strings"""
        return EducationExperience(
            Institution=model.get('Institution', ''),
            InstitutionDescription=RawProfile.make_description_model(model.get('InstitutionDescription', '')),
            Specialization=model.get('Specialization', ''),
            SpecializationDescription=RawProfile.make_description_model(model.get('SpecializationDescription', '')),
            Degree=model.get('Degree', ''),
            Start=RawProfile.make_date(model.get('Start')),
            End=RawProfile.make_date(model.get('End')),
        )
