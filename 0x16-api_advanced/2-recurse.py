#!/usr/bin/python3
""" returns all hot title for a given subreddit (recursive) """
import json
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """ recursive all hot titles """
    headers = {'User-Agent': 'test'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    sub_res = requests.get(url, headers=headers)
    if count > 1 and after is None:
        return (hot_list)
    if after is None:
        if sub_res.status_code == 200:
            hot = sub_res.json().get('data').get('children')
            for el in hot:
                hot_list.append(el.get("data").get("title"))
            after = sub_res.json().get("data").get("after")
            recurse(subreddit, hot, after, count + 1)

        else:
            return (None)
    else:
        url_next = "https://www.reddit.com/r/{}/hot.json?after={}".format(
               subreddit, after)
        next_el = requests.get(url_next, headers=headers)
        for el in next_el.json().get("data").get("children"):
            hot_list.append(el.get("data").get("title"))
        after = next_el.json().get("data").get("after")
        recurse(subreddit, hot_list, after, count + 1)
    return (hot_list)
