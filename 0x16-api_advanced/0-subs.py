#!/usr/bin/python3
""" Returns subs to a subreddit """
import requests


def number_of_subscribers(subreddit):
    """ returns num of subs """
    headers = {'User-Agent': 'test'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        sub_json = res.json().get('data')
        subs = sub_json.get('subscribers')
        return (subs)
    else:
        return (0)
