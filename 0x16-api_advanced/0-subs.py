#!/usr/bin/python3
"""
module for task 0
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns number of subscribers in a subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    h = requests.utils.default_headers()
    h.update({'User-Agent': 'My User Agent 1.0'})
    r = requests.get(url, headers=h).json()
    subs = r.get('data', {}).get('subscribers')
    if not subs:
        return 0
    return subs
