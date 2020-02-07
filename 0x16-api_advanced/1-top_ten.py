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

        url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
        headers = {"user-agent": "Nicolás"}
        request = requests.get(url, headers=headers, allow_redirects=False)

        if (request.status_code != 200):
            print(None)

        request_json = request.json()
        data = request_json.get("data")
        children = data.get("children")

        for counter in children:
            print(counter.get("data").get("title"))

    except Exception as err:
        print(None)
