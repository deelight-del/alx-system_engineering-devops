#!/usr/bin/python3
""" Querying for the amount of users
in a subredding"""


import requests


def number_of_subscribers(subreddit):
    """ Function to retrieve the number of
    subscribers of a given reddit

    Parameters:
        subreddit - subreddit to check.

    Return:
        Number of subscribers or 0 if not found
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/102.0.0.0 Safari/537.36'
            }
    r = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            allow_redirects=False,
            headers=headers
            )
    if r.status_code != 200:
        return 0
    return (r.json()["data"]["subscribers"])
