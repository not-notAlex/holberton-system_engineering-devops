#!/usr/bin/python3
"""
module for task 1
"""
import requests


def top_ten(subreddit):
    """
    returns top 10 hot posts in subreddit
    """
    h = requests.utils.default_headers()
    h.update({'User-Agent': 'My User Agent 1.0'})
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    r = requests.get(url, headers=h).json()
    result = r.get('data', {}).get('children', [])
    if not result:
        print(None)
    for i in result:
        print(i.get('data').get('title'))
