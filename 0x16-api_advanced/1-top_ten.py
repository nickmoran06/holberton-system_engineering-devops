#!/usr/bin/python3
"""
Module using the Reddit API
"""
import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit.
    """
    try:
        if subreddit is None or type(subreddit) is not str:
            print(None)

        url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
        request = requests.get(url, headers={"User_agent": "Nicolás"})

        if (request.status_code != 200):
            print(None)

        data = request.json().get("data")
        children = data.get("children")

        for counter in children:
            print(counter.get("data").get("title"))

    except Exception as err:
        print(None)
