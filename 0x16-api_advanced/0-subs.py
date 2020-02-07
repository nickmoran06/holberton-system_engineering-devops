#!/usr/bin/python3
"""
Module using the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of
    subscribers for a given subreddit.
    """
    try:
        if subreddit is None or type(subreddit) is not str:
            return (0)

        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {"User-Agent": "Nicolas"}
        request = requests.get(url, headers=headers, allow_redirects=False)

        if request.status_code is not 200:
            return (0)

        subscribers = request.json().get("data").get("subscribers")
        return (subscribers)

    except Exception as err:
        return (0)
