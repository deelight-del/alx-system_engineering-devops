#!/usr/bin/python3
""" Querying for the top 10 hottest posts
in a subreddit"""
import requests


def top_ten(subreddit):
    """ Function to retrieve the top 10 hottest
    posts of a givne subreddit

    Parameters:
        subreddit - subreddit to check.

    Return:
        PRINT titles of top 10 hottest posts, or None
    """
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/102.0.0.0 Safari/537.36'
            }
    r = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10",
            allow_redirects=False,
            )
    if r.status_code != 200:
        print("None")
        return
    for child in r.json()["data"]["children"][:-1]:
        print(child["data"]["title"])
