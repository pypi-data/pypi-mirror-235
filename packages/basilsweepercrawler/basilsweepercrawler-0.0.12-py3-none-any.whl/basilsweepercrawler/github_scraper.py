import json
import requests
import time
import os
from datetime import datetime
from typing import List, Dict, Optional, Any

from searchdatamodels import Candidate, DescriptionModel
from searchdatamodels.search_classes import ContactInfo

TOKEN = os.getenv('YOUR_GITHUB_TOKEN')


class GitHubUser:
    """
    Represents a user on GitHub with methods to fetch user's profile data.

    Parameters:
    ----------
    username : str
        The username of the GitHub user.
    token : str
        The GitHub personal access token for authentication.
    """

    def __init__(self, username: str, token: str):
        self.username = username
        self.user_url = f'https://api.github.com/users/{self.username}'
        self.headers = {'Authorization': f'token {token}'}

    def fetch_user_profile(self) -> Dict[str, Any]:
        """
        Fetch the user's profile data from GitHub.

        Returns:
        ----------
        dict
            The user's profile data in JSON format.
        """
        response = requests.get(self.user_url, headers=self.headers)
        if response.status_code != 200:
            raise Exception(
                f"Error fetching profile for {self.username}. Status Code: {response.status_code}")
        return response.json()

    def fetch_user_social_accounts(self) -> Dict[str, Any]:
        """
        Fetch the user's social account listed on their GitHub profile.

        Returns:
        ----------
        dict
            The user's social account data in JSON format.
        """
        response = requests.get(
            self.user_url + "/social_accounts", headers=self.headers)
        if response.status_code != 200:
            raise Exception(
                f"Error fetching social accounts for {self.username}. Status Code: {response.status_code}")
        return response.json()


def check_rate_limit(response: requests.Response) -> None:
    """
    Checks and displays the GitHub API rate limit details from the response headers.

    Parameters:
    ----------
    response : requests.Response
        The response from an API request containing rate limit headers.
    """
    headers = ['X-RateLimit-Limit',
               'X-RateLimit-Remaining', 'X-RateLimit-Reset']
    if all(header in response.headers for header in headers):
        print(f"Rate Limit: {response.headers['X-RateLimit-Limit']}")
        print(
            f"Remaining Requests: {response.headers['X-RateLimit-Remaining']}")
        reset_time = datetime.utcfromtimestamp(
            int(response.headers['X-RateLimit-Reset']))
        print(f"Reset Time: {reset_time}")
    else:
        print("Rate limit headers not found!")


def search_users_by_tag(token: str, tag: str, max_users: int) -> List[str]:
    """
    Searches GitHub users based on a specific keyword or tag.

    Parameters:
    ----------
    token : str
        The GitHub personal access token for authentication.
    tag : str
        The search keyword/tag to filter users by.
    max_users : int
        Maximum number of users to fetch.

    Returns:
    ----------
    list
        List of usernames matching the given tag.
    """
    per_page = 100
    page_number = 1
    all_usernames: List[str] = []
    headers = {'Authorization': f'token {token}'}

    while len(all_usernames) < max_users:
        search_url = f'https://api.github.com/search/users?q={tag}&per_page={per_page}&page={page_number}'
        response = requests.get(search_url, headers=headers)

        if response.status_code != 200:
            check_rate_limit(response)
            raise Exception(
                f"Error fetching users for tag {tag}. Status Code: {response.status_code}")

        data = response.json()
        usernames = [item['login'] for item in data.get('items', [])]

        if not usernames:
            break

        all_usernames.extend(usernames)
        page_number += 1
        time.sleep(1)

    return all_usernames[:max_users]


def scrape_github_user(token: Optional[str], username: str):
    if not token:
        print("GitHub token not provided!")
        return

    user = GitHubUser(username, token)
    data = {}
    try:
        data = user.fetch_user_profile()
    except Exception as e:
        print(e)

    if data and data.get('type') == 'User':
        try:
            social_accounts = user.fetch_user_social_accounts()
        except Exception as e:
            print(e)

        if social_accounts:
            data['social_accounts'] = social_accounts
        return data
    else:
        return {}


def make_candidate(
        data: dict,
        username: str,
        enforce_email: bool = True,
        enforce_summary: bool = True
) -> Candidate | None:
    """
    Given a user data as a dict returns a Candidate instance

    Arguments
    ---------
    data : dict
        The user directly from JSON
    username : str
        The username of the GitHub user
    enforce_email : bool
        Returns None if the email is not present
    enforce_summary : bool
        Returns None if the summary is not present

    Returns
    -------
    Candidate
        A candidate instance
    """
    if data and data["name"] != None:
        if enforce_email and data["email"] is None:
            return None
        if enforce_summary and data["bio"] is None:
            return None

        sources = ["https://github.com/" + username]
        # if user specifies their blog
        if data["blog"] != "":
            sources.append(data["blog"])
        if "social_accounts" in data:
            for social_account in data["social_accounts"]:
                sources.append(social_account["url"])

        contact_info_list = []
        if data["email"]:
            contact_info_list.append(ContactInfo(
                Type="email",
                Value=data["email"]
            ))

        return Candidate(
            Name=data["name"],
            Location=data["location"] if data["location"] != None else "",
            Picture=data["avatar_url"] if data["avatar_url"] != None else "",
            Sources=sources,
            ContactInfoList=contact_info_list,
            Summary=DescriptionModel(Text=data["bio"]) if data["bio"] != None else "",
            ExternalSummaryStr=data["bio"] if data["bio"] != None else "",
            ProjectList=[],
        )


def run_github_scraper(
        token: Optional[str],
        tag: str,
        max_users: int,
        return_as_candidate: Optional[bool] = False,
        save_folder: Optional[str] = os.getcwd(),
) -> List[dict] | List[Candidate]:
    """
    Main function to run the GitHub scraper.

    Parameters:
    ----------
    token : Optional[str]
        The GitHub personal access token for authentication. If None, scraping does not occur.
    tag : str
        The search keyword/tag to search users by.
    max_users : int
        Maximum number of users to fetch and save.
    return_as_candidate : Optional[bool]
        Returns a Candidate instance
    save_folder : Optional[str]
        Saves results in the given folder and, if none, does not save results
    """
    if not token:
        print("GitHub token not provided!")
        return []

    usernames = search_users_by_tag(token, tag, max_users)
    print(f'Found {len(usernames)} users related to tag "{tag}"')

    result = []
    for username in usernames:
        data = scrape_github_user(token, username)

        if data:
            if save_folder is not None:
                with open(f'{os.path.join(save_folder, username)}.json', 'w') as json_file:
                    json.dump(data, json_file)
                print(f'Saved data for user {username} to {username}.json')
            result.append((data, username))
        else:
            print(f'Skipped non-User type for: {username}')

        time.sleep(1)

    print("----- DONE -----")
    if return_as_candidate:
        result_cand = []
        for _data, _username in result:
            c = make_candidate(_data, _username)
            if c:
                result_cand.append(c)
        return result_cand
    else:
        return [a[0] for a in result]
