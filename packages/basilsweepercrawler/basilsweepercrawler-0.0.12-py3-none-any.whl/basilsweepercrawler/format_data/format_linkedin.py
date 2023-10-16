import logging
import json
from typing import List
from itertools import zip_longest

from basilsweepercrawler.format_data.format_candidate import RawProfile, CandidateSchema
from basilsweepercrawler.format_data.exceptions import AllFailedError
from searchdatamodels import Candidate, DescriptionModel

logger = logging.getLogger(__name__)


class RawLinkedinProfile(RawProfile):
    """
    Raw LinedIn profile as provided by the scraper. Extends RawProfile
    """
    @property
    def json_system_msgs(self):
        return [
            'You are given a JSON schema and a plain text input. Your goal is to return a JSON string'
            'which respects the given schema and contains ALL the information present in the text',
            'For example:' + self.before_schema +
            json.dumps(CandidateSchema.work_exp_schema) +
            self.before_prompt +
            'Experience\nLead data scientist at Apple Inc.\nDec 2019 - Nov 20222 years 11 months\nLead data scientist\n'
            'I lead the Data Science team for the Apple Store. We specialize in ads, ranking and monetization.' +
            self.before_json +
            json.dumps({
                'Institution': 'Apple Inc.',
                'Specialization': 'Lead data scientist',
                'SpecializationDescription':
                    "I lead the Data Science team for the Apple Store. We specialize in ads, ranking and monetization.",
                'Start': '2019-12-01',
                'End': '2022-11-01',
            })
        ]

    @property
    def text_system_msgs(self):
        return []

    @property
    def list_system_msgs(self):
        return [
            'You are given text containing one or more elements prepended with an header that describes them '
            'and you should output a list of items with that header skipping unnecessary line breaks or punctuation.',
            'For example:' + self.before_prompt +
            '"Languages\nEnglish\n-\nFrench\n-\nSpanish\n-"' +
            self.before_list +
            '["English language", "French language", "Spanish language"]'
        ]

    @staticmethod
    def delete_duplicates(experience_list: List[dict]) -> List[dict]:
        """
        Deletes duplicate elements in a list of dicts by comparing field by field

        Arguments
        ---------
        experience_list : List[dict]
            Input list of dicts

        Returns
        -------
            List of dicts which is duplicate-free
        """
        new_list = experience_list
        for i, elem in enumerate(new_list):
            for j in range(len(new_list) - 1, i, -1):
                other = new_list[j]
                if all(
                    a == b for a, b in zip_longest(elem.values(), other.values())
                ):
                    del new_list[j]

        return new_list

    def make_candidate(self) -> Candidate:
        """
        Returns a Candidate instance corresponding to the profile scraped

        Returns
        -------
        Candidate
            an instance of the Candidate data model

        Raises
        ------
        OpeAICall.AllFailedError
            If the OpenAI call is not successful

        """
        try:
            name = self.profile['name']
            source = self.profile['url']
        except KeyError:
            logger.error('Missing name or url, profile invalid')
            raise AllFailedError('Missing name or url, profile invalid', AllFailedError.FATAL_ERROR)

        bio = self.profile.get('biography')
        all_exp = self.profile.get('experiences')
        if all_exp is None:
            return Candidate(
                Name=name,
                Sources=[source],
                ExternalSummaryStr=bio if bio else ''
            )
        else:
            fields = {
                'Skills': [],
                'WorkExperienceList': [],
                'EducationExperienceList': [],
                'ProjectList': [],
                'Additional': []
            }
            for exp_type, content in all_exp.items():
                if exp_type == 'Education':
                    schema = CandidateSchema.edu_exp_schema
                    for entry in content:
                        fields['EducationExperienceList'].append(self.text_to_schema(
                            text=entry,
                            schema=schema
                        ))
                elif exp_type == 'Experience':
                    schema = CandidateSchema.work_exp_schema
                    for entry in content:
                        fields['WorkExperienceList'].append(self.text_to_schema(
                            text=entry,
                            schema=schema
                        ))
                elif exp_type == 'Licenses & Certifications':
                    schema = CandidateSchema.edu_exp_schema
                    for entry in content:
                        fields['EducationExperienceList'].append(self.text_to_schema(
                            text=entry,
                            schema=schema,
                            additional_msgs=[
                                'Specify in SpecializationDescription that this is a License or Certification']
                        ))
                elif exp_type == 'Publications':
                    for entry in content:
                        fields['ProjectList'] = fields['ProjectList'] + self.text_to_list(
                            text=entry
                        )
                elif exp_type == 'Courses':
                    schema = CandidateSchema.edu_exp_schema
                    for entry in content:
                        fields['EducationExperienceList'].append(self.text_to_schema(
                            text=entry,
                            schema=schema
                        ))
                elif exp_type == 'Languages':
                    for entry in content:
                        fields['Skills'] = fields['Skills'] + self.text_to_list(
                            text=entry
                        )
                elif exp_type == 'Organizations':
                    schema = CandidateSchema.work_exp_schema
                    for entry in content:
                        fields['WorkExperienceList'].append(self.text_to_schema(
                            text=entry,
                            schema=schema,
                            additional_msgs=[
                                'Specify in SpecializationDescription that this is an Organization']
                        ))
                else:
                    if content:
                        logger.info(f'Found a field that we did not expect: {exp_type}')
                        schema = CandidateSchema.candidate_schema
                        for entry in content:
                            fields['Additional'].append(self.text_to_schema(
                                text=entry,
                                schema=schema,
                                additional_msgs=['Find the property in this schema that is'
                                                 f'better suited for {exp_type}, output a valid JSON '
                                                 f'string filling the Name field with XXX.']
                            ))

            for additional in fields['Additional']:
                for k, v in additional.items():
                    if k != 'Name':
                        try:
                            fields[k] += v
                        except KeyError as err:
                            logger.warning(f'Produced additional field which is non existent: {err}')
                            continue

            # Sometimes various sections appear duplicated
            fields['WorkExperienceList'] = self.delete_duplicates(fields['WorkExperienceList'])
            fields['EducationExperienceList'] = self.delete_duplicates(fields['EducationExperienceList'])

            return Candidate(
                Name=name,
                Sources=[source],
                ExternalSummaryStr=bio if bio else '',
                WorkExperienceList=[self.make_work_experience(w) for w in fields['WorkExperienceList']],
                EducationExperienceList=[self.make_education_experience(e) for e in fields['EducationExperienceList']],
                ProjectList=[self.make_description_model(p) for p in set(fields['ProjectList'])],
                Skills=list(set(fields['Skills'])),
            )