#!/usr/bin/python3
"""
module for task 2
"""
import requests


def recurse(subreddit, hot_list=[], after="tmp"):
    """
    returns list of hot titles in a subreddit
    """
    h = requests.utils.default_headers()
    h.update({'User-Agent': 'My User Agent 1.0'})
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after != "tmp":
        url = url + "?after={}".format(after)
    r = requests.get(url, headers=h, allow_redirects=False)
    result = r.json().get('data', {}).get('children', [])
    if not result:
        return hot_list
    for i in result:
        hot_list.append(i.get('data').get('title'))
    after = r.json().get('data').get('after')
    if not after:
        return hot_list
    return (recurse(subreddit, hot_list, after))
