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
    r = requests.get(
            f"https://www.reddit.com/r/{subreddit}/about.json",
            allow_redirects=False
            )
    #if r.status_code != 200:
    #    return 0
    return r.json().get("data", dict()).get("subscribers", 0)
