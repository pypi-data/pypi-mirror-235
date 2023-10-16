import json
import os
import re
from typing import List, Optional, Literal
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup

from searchdatamodels import Candidate, WorkExperience, DescriptionModel

MAX_RESULT_PER_PAGE = 100

API_URL = '\
https://api.stackexchange.com/2.3/users?page={page}&pagesize={max}&order=desc&sort={sortby}&site={site}'
API_URL_NAME = '\
https://api.stackexchange.com/2.3/users?page={page}&pagesize={max}&order=desc&sort={sortby}&inname={name}&site={site}'


StackExchangeSite = Literal[
    # There are more but these are the most relevant ones
    'stackoverflow', 'physics', 'superuser', 'serverfault', 'mathematics', 'academia',
    'tex', 'mathoverflow', 'unix', 'gamedev', 'music', 'dba', 'quant', 'webmasters',
    'webapps', 'photo', 'stats', 'ux', 'money', 'askubuntu', 'wordpress', 'cstheory',
    'apple', 'softwareengineering', 'android', 'electronics', 'sound', 'video',
    'graphicdesign', 'biology', 'academia', 'workplace', 'blender', 'datascience',
    'quantumcomputing'
]
SortType = Literal['reputation', 'modified', 'creation']


@dataclass
class ResultWithPage:
    """Contains the next page to try and the result"""
    result: List[dict] | List[Candidate]
    page: Optional[int] = 1


def run_stackexchange_scraper(
        max_users: int,
        site: Optional[StackExchangeSite] = 'stackoverflow',
        sortby: Optional[SortType] = 'reputation',
        name: Optional[str] = None,
        save_folder: Optional[str] = None,
        return_as_candidate: Optional[bool] = False,
        start_at_page: Optional[int] = 1
) -> ResultWithPage:
    """
    Runs the StackExchange scraper by using the users API

    Arguments
    --------
    max_users : int
        Max number of users to retrieve
    site : StackExchangeSite
        The site to scrape from e.g. "stackoverflow", "physics", ...
    sortby : Optional[SortType]
        Sort by reputation or date of last modification
    name : Optional[str]
        If None just searches for any user, otherwise searcher for users matching name
    save_folder : Optional[str]
        If not None saves results in json format to the given folder
    return_as_candidate : Optional[bool]
        If True return results as Candidate instances rather than plain dicts
    start_at_page : Optional[int]
        Starts at another page to pick up from previous searcher

    Returns
    ------
    ResultWithPage
        A list of user data in JSON or Candidate with the next page to try

    """

    def get_url(page_no, max_no=MAX_RESULT_PER_PAGE):
        if name:
            return API_URL_NAME.format(
                page=page_no,
                max=max_no,
                sortby=sortby,
                site=site,
                name=name
            )
        else:
            return API_URL.format(
                page=page_no,
                max=max_no,
                sortby=sortby,
                site=site
            )

    missing = max_users
    found = []
    page_no = start_at_page
    quota_remaining = 300
    while missing > 0:
        getting = min(MAX_RESULT_PER_PAGE, missing)
        print(f'Fetching {getting} profiles sorted by "{sortby}" in pag. {page_no}.')
        response = requests.get(get_url(page_no, getting))
        if response.status_code != 200:
            print(f'Error fetching profile for {sortby} in pag. {page_no}. Status Code: {response.text}')
            break
        else:
            page_no += 1
            try:
                response_json = response.json()
                retrieved = response_json['items']
            except KeyError:
                print('key "items" not found in result')
                break
            else:
                missing -= len(retrieved)
                found += retrieved
                retrieved_plus = [get_additional_data(r) for r in retrieved]
                if save_folder:
                    to_disk(retrieved_plus, save_folder, site=site)

            try:
                quota_remaining = int(response_json['quota_remaining'])
                if quota_remaining == 0:
                    print('The available quota has terminated, breaking from loop')
                    break
                else:
                    print(f'Quota remaining: {quota_remaining}')
            except KeyError:
                print('Error: quota_remaining not found, assuming it is the same as before minus one')
                quota_remaining -= 1

    print(f'finished scraping profiles. Pick up from page: {page_no}')
    if return_as_candidate:
        return ResultWithPage(page=page_no, result=[make_candidate(f) for f in found])
    else:
        return ResultWithPage(page=page_no, result=found)


def get_additional_data(user_json: dict) -> dict:
    """
    Takes the JSON output by the API and tries to get additional data from the site

    Arguments
    ---------
    user_json : dict
        The JSON output by the API

    Returns
    -------
    dict
        The same user with additional data added
    """
    def interesting_link(url: str) -> bool:
        if re.search('|'.join([
            'github', 'twitter', 'facebook', 'instagram', 'gitlab',
        ]), url) and not re.search('|'.join([
            'stackoverflow', 'stackexchange'  # these would be just the site links
        ]), url):
            return True
        else:
            return False

    try:
        site = user_json['link']
    except KeyError:
        return user_json
    else:
        user_site = requests.get(site)
        if user_site.status_code != 200:
            return user_json
        else:
            user_soup = BeautifulSoup(user_site.text, 'html.parser')
            uls = user_soup.find_all('ul')
            found_links = []
            for ul in uls:
                links = [a['href'] for a in ul.find_all('a', href=re.compile('.*'))]
                if any(interesting_link(l) for l in links):
                    # There are some links which are interesting and others are just links to other pages in SE
                    found_links = links
                    break
            desc = user_soup.find('div', class_='s-prose fc-medium js-about-me-content')
            if desc:
                user_json['found_description'] = desc.text
            if found_links:
                user_json['found_extra_links'] = found_links

            return user_json


def to_disk(list_of_users: List[dict], save_folder: str, site: Optional[str] = 'stackexchange'):
    """
    Saves a list of user to disk

    Arguments
    ---------
    list_of_users : List[dict]
        The list of users to save
    save_folder : str
        The folder
    site : str
        The site it comes from
    """
    try:
        for u in list_of_users:
            try:
                u_name = u['user_id']
            except KeyError:
                u_name = hash(str(u))
            with open(os.path.join(save_folder, f'{site}_{u_name}.json'), 'w') as json_file:
                json.dump(u, json_file)
    except FileNotFoundError as e:
        print(f'Could not save files in {save_folder}: FileNotFoundError({e})')
    else:
        print(f'saved {len(list_of_users)} files in {save_folder}')


def make_candidate(user: dict) -> Candidate:
    """
    Takes a user as returned by the API and makes a candidate instance

    Arguments
    ---------
    user : dict
        The output of the API

    Returns
    -------
    Candidate
        The corresponding candidate instance
    """
    name = user.get('display_name', 'unknown')
    location = user.get('location')
    w_exp = []
    try:
        coll = user['collectives']
        for c in coll:
            c_data = c['collective']
            w_exp.append(WorkExperience(
                # Some users are part of a "StackExchange collective." We consider it as some sort of work experience
                Institution=c_data['name'] + ' StackExchange collective',
                InstututionDescription=c_data['description'],
                Specialization=c['role']
            ))
    except KeyError:
        pass

    sources = []
    for source_field in ['link', 'website_url']:
        try:
            sources.append(user[source_field])
        except KeyError:
            pass
    if 'found_extra_links' in user:
        sources += user['found_extra_links']

    desc = user.get('found_description', '')

    image = user.get('profile_image')

    return Candidate(
        Name=name,
        ExternalSummaryStr=desc,
        Sources=list(set(sources)),
        WorkExperienceList=w_exp,
        Location=location,
        Picture=image
    )