import os
from typing import Dict, Any, Literal, Optional, List
import requests
import json
import time
from dataclasses import dataclass

from searchdatamodels import Candidate, WorkExperience

# There are more entities, but we probably don't care about most of them
Entity = Literal['organizations', 'people', 'jobs']


class CrunchbaseRequest:
    """
    Represents a request on Crunchbase (either a search or an entity lookup) with methods to fetch its data.

    Parameters
    ----------
    user_key : str
        The token used for the Crunchbase API.
    query_value : str
        If used for an entity lookup it's the id of the entity, if used for a search it's a keyword / tag
    entity_type : Entity
        The type of entity (organization, people, ...)
    """

    def __init__(self, user_key: str, query_value: str, entity_type: Entity):
        self.entity_type = entity_type
        self.query_value = query_value

        API_URL = 'https://api.crunchbase.com/api/v4'
        if self.entity_type == 'organizations':
            field_ids = ['identifier', 'company_type', 'description', 'name', 'website', 'location_identifiers']
            card_ids = []  # ['jobs']
        elif self.entity_type == 'people':
            # Full list of fields:
            # https://app.swaggerhub.com/apis-docs/Crunchbase/crunchbase-enterprise_api/1.0.3#/Search/post_searches_people
            field_ids = [
                'identifier',
                'name', 'first_name', 'last_name', 'middle_name',
                'linkedin', 'facebook', 'twitter', 'website_url', 'website',
                'image_id', 'image_url',
                'primary_job_title', 'primary_organization',
                'location_group_identifiers', 'location_identifiers',
                'description', 'updated_at'
            ]
            card_ids = []
        else:
            raise ValueError(f'Entity type {self.entity_type} not supported')

        field_ids_s = ','.join(field_ids)
        card_ids_s = ','.join(card_ids)

        self.lookup_url = f'{API_URL}/entities/{entity_type}/{query_value}?card_ids={card_ids_s}&field_ids={field_ids_s}'
        self.search_url = f'{API_URL}/searches/{entity_type}'
        self.headers = {'X-cb-user-key': user_key, 'accept': 'application/json'}
        self.search_headers = self.headers | {'Content-Type': 'application/json'}

        self.search_body = {
            'field_ids': field_ids,
            'query': [{
                'type': 'predicate',
                'field_id': 'description',
                'operator_id': 'contains',
                'values': query_value,
            }],
            'limit': 1000,
        }

    def fetch_entity_profile(self) -> Dict[str, Any]:
        """
        Fetch the entity's data from Crunchbase.

        Returns
        -------
        dict
            The entity's data in JSON format.
        """
        response = requests.get(self.lookup_url, headers=self.headers)
        if response.status_code != 200:
            raise Exception(
                f"Error fetching profile for {self.entity_type}: {self.query_value}. Status Code: {response.status_code}")
        return response.json()

    def perform_search(self, max_entities: int = 1000, after_id: Optional[str] = None) -> List[dict]:
        """
        Performs a search with the query provided at object creation

        Arguments
        --------
        max_entities : int
            Max number of entities to return
        after_id : Optional[str]
            uuid of the entity from which we start returning new entities

        Returns
        -------
        list[dict]
            A list of matching entities
        """
        self.search_body['limit'] = min(max_entities, 1000)
        if after_id:
            search_body = self.search_body | {'after_id': after_id}
        else:
            search_body = self.search_body
        response = requests.post(self.search_url, headers=self.search_headers, data=json.dumps(search_body))
        if response.status_code != 200:
            raise Exception(
                f'Error performing search for {self.entity_type}: {self.query_value}. '
                f'Status Code: {response.status_code}\n'
                f'Response: {response.text}'
            )
        else:
            data = response.json()
            try:
                results = data['entities']
            except KeyError:
                raise Exception(f'Search for {self.entity_type}: {self.query_value} produced an invalid JSON: {data}')
            else:
                return results


def make_candidate(raw_data: dict) -> Candidate:
    """
    Given a dict of JSON data returns a Candidate instance
    Arguments
    ---------
    data : dict
        The JSON data

    Returns
    -------
    Candidate
        The candidate instance
    """
    def get_path(path: str, json: dict) -> Any:
        path_list = path.split('.')
        j = json
        for p in path_list:
            if isinstance(j, dict):
                j = j[p]
            else:
                raise KeyError(p)
        return j

    data = raw_data['properties']

    sources = {'https://www.crunchbase.com/person/' + raw_data['uuid']}
    for path in [
        'website_url',
        'website.value',
        'facebook.value',
        'twitter.value'
    ]:
        try:
            sources.add(get_path(path, data))
        except KeyError:
            print(f'data {path} not found in source')
            continue

    sources = list(sources)

    try:
        name = data['name']
    except KeyError:
        try:
            name = get_path('identifier.value', data)
        except KeyError:
            print('name not found!')
            name = 'unknown'

    try:
        if 'location_identifiers' in data:
            loc_group = data['location_identifiers']
        else:
            loc_group = data['location_group_identifier']
    except KeyError:
        location = None
    else:
        loc_list = []
        for loc in loc_group:
            try:
                loc_list.append(loc['value'])
            except KeyError:
                continue

        if loc_list:
            location = ', '.join(loc_list)
        else:
            location = None

    try:
        picture = data['image_url']
    except KeyError:
        picture = None

    ext_summary = data.get('description', '')

    try:
        work = get_path('primary_organization.value', data)
        job_title = data['primary_job_title']
        work_exp = WorkExperience(
            Institution=work,
            Specialization=job_title,
        )
    except KeyError as k:
        print(f'Work experience not found: missing key {k}')
        work_exp = WorkExperience(Institution=None, Specialization=None)

    return Candidate(
        Name=name,
        Location=location,
        Picture=picture,
        Sources=sources,
        ExternalSummaryStr=ext_summary,
        WorkExperienceList=[work_exp],
    )


def scrape_crunchbase_entity(
        token: str,
        entity_id: str,
        entity_type: Optional[Entity] = 'people',
        save_folder: Optional[str] = None,
        return_as_candidate: Optional[bool] = False,
) -> dict | Candidate:
    """
    Scrape a single entity given its uuid or permalink

    Arguments
    --------
    token : str
        The API token
    entity_id : str
        The entity uuid or permalink
    entity_type : Optional[Entity]
        The entity type
    save_folder : Optional[str]
        Optionally save results to this folder
    return_as_candidate : Optional[bool]
        If True returns a Candidate instances otherwise (default) returns raw data from the Crunchbase API

    Returns
    -------
    dict | Candidate
        A dict from the JSON result or a corresponding Candidate instance
    """

    request = CrunchbaseRequest(token, entity_id, entity_type)
    try:
        data = request.fetch_entity_profile()
    except Exception as e:
        print(e)
        return {}

    if return_as_candidate and entity_type != 'people':
        raise ValueError('can set return_as_candidate=True only for the "people" entity type')

    try:
        identifier = data['properties']['identifier']
        name = identifier['permalink'] if 'permalink' in identifier else data['uuid']

        if save_folder is not None:
            try:
                with open(os.path.join(save_folder, f'{name}.json'), 'w') as json_file:
                    json.dump(data, json_file)
            except FileNotFoundError as e:
                print(f'Could not save contents of {name}.json: FileNotFoundError({e})')
            else:
                print(f'Saved data for {entity_type} {name} to {name}.json')

        if return_as_candidate:
            return make_candidate(data)
        else:
            return data

    except KeyError as e:
        print(f'Skipped invalid data for this entity, missing key: {e}')
        return {}


@dataclass
class ResultWithAfterId:
    """Contains the id of the last candidate returned and the result"""
    result: List[dict] | List[Candidate]
    after_id: Optional[str] = None


def run_crunchbase_scraper(
        token: Optional[str],
        tag: str,
        max_entities: int,
        entity_type: Optional[Entity] = 'people',
        save_folder: Optional[str] = None,
        return_as_candidate: Optional[bool] = False,
        after_id: Optional[str] = None,
) -> ResultWithAfterId:
    """
    Main function to run the Crunchbase scraper.

    Parameters
    ----------
    token : Optional[str]
        The Crunchbase personal access token for authentication. If None, taken from os.environ['CRUNCHBASE_TOKEN'].
    tag : str
        The search keyword/tag to search entities by.
    max_entities : int
        Maximum number of entities to fetch and save.
    entity_type : Optional[Entity]
        Type of entity to be retrieved
    save_folder : Optional[str]
        Optionally the folder where to save the results
    return_as_candidate : Optional[bool]
        If True returns a list of Candidate instances otherwise (default) returns raw data from the Crunchbase API
    after_id : Optional[str]
        The uuid of the last result in the search for picking up from there in a second search

    Returns
    ------
    ResultWithAfterId
        A list of dict from the JSON result or a list of the corresponding Candidate instances with the
        uuid of the last entity
    """
    if not token:
        try:
            token = os.environ['CRUNCHBASE_TOKEN']
        except KeyError:
            print("Crunchbase token not provided!")
            return ResultWithAfterId(result=[])

    if return_as_candidate and entity_type != 'people':
        raise ValueError('can set return_as_candidate=True only for the "people" entity type')

    final = make_candidate if return_as_candidate else lambda _x: _x

    request = CrunchbaseRequest(token, tag, entity_type)
    entities = request.perform_search(max_entities, after_id=after_id)
    print(f'Found {len(entities)} users related to tag "{tag}"')

    to_return = []
    last_id = None
    for entity in entities:
        try:
            identifier = entity['properties']['identifier']
            last_id = entity['uuid']
            name = identifier['permalink'] if 'permalink' in identifier else entity['uuid']
            to_return.append(final(entity))

            if save_folder is not None:
                try:
                    with open(os.path.join(save_folder, f'{name}.json'), 'w') as json_file:
                        json.dump(entity, json_file)
                except FileNotFoundError as e:
                    print(f'Could not save contents of {name}.json: FileNotFoundError({e})')
                else:
                    print(f'Saved data for {entity_type} {name} to {name}.json')

        except KeyError as e:
            print(f'Skipped invalid data for this entity, missing key: {e}')

        time.sleep(1)

    print("----- DONE -----")
    return ResultWithAfterId(result=to_return, after_id=last_id)

