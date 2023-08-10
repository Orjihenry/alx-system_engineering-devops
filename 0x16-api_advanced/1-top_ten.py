#!/usr/bin/python3
"""
    Prints first 10 hottest posts of a given sureddit
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "MyRedditBot/2.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])

    for i, post in enumerate(posts[:10], start=1):
        title = post.get("data", {}).get("title")
        print(f"{i}. {title}")
