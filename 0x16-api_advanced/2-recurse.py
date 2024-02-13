#!/usr/bin/python3
""" Querying for all of the  hottest posts
in a subreddit"""
import requests


def recurse(subreddit, hot_list=[], params={}):
    """ Function to retrieve the top 10 hottest
    posts of a givne subreddit

    Parameters:
        subreddit - subreddit to check.
        hot_list - list of hot titles.

    Return:
        PRINT titles of top 10 hottest posts, or None
    """
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/102.0.0.0 Safari/537.36'
            }
    r = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json",
            allow_redirects=False,
            headers=headers,
            params=params
            )
    if r.status_code != 200:
        return
    for child in r.json()["data"]["children"][:-1]:
        hot_list.append(child["data"]["title"])
    if r.json()["data"]["after"] is None:
        return hot_list
    after_value = r.json()["data"]["after"]
    return recurse(subreddit, hot_list, {"after": after_value})
