#!/usr/bin/python3
"""
    Query list of all hot posts of a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[]):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyRedditBot/2.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    if not posts:
        return hot_list

    title_list = [post.get("data", {}).get("title") for post in posts]
    hot_list.extend(title_list)

    after = data.get("data", {}).get("after")
    if after:
        return recurse(subreddit, hot_list=hot_list)
    else:
        return hot_list
