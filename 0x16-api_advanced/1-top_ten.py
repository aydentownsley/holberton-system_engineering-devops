#!/usr/bin/python3
""" get top ten titles from hot """
import json
import requests


def top_ten(subreddit):
    """ top ten titles """
    headers = {'User-Agent': 'test'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    sub_res = requests.get(url, headers=headers)
    if sub_res.status_code == 200:
        hot = sub_res.json().get('data').get('children')
        for el in hot:
            print(el.get('data').get('title'))

    else:
        print(None)
