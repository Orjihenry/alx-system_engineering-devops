#!/usr/bin/python3
"""
    Script that GETS num of subs of a given subredit.
    Returns 0 if no valid subredis is given.
"""
import requests


def number_of_subscribers(subreddit):

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'MyRedditBot/2.0'}  # Custom User-Agent header
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        subscribers = data['data']['subscribers']  # number of subs

        return subscribers
    else:
        return 0
