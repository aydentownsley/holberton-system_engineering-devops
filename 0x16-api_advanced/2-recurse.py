#!/usr/bin/python3
""" returns all hot title for a given subreddit (recursive) """
import json
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """ recursive all hot titles """
    if count > 1 and after is None:
        return (hot_list)
    elif after is None:
        sub_res = requests.get(
            'https://reddit.com/r/{}/hot.json'.format(subreddit),
            headers={'User-agent': 'test'})
        if sub_res.status_code == 200:
            hot = requests.get(
                'https://reddit.com/r/{}/hot.json'.format(subreddit),
                headers={'User-agent': 'test'})
            for el in hot.json().get('data').get('children'):
                hot_list.append(el.get('data').get('title'))
            after = hot.json().get('data').get('after')
            recurse(subreddit, hot_list, after, count + 1)
        else:
            return (None)
    else:
        hot = requests.get(
            'https://reddit.com/r/{}/hot.json?after={}'.format(
             subreddit, after), headers={'User-agent': 'test'})
        for el in hot.json().get('data').get('children'):
            hot_list.append(el.get('data').get('title'))
        after = hot.json().get('data').get('after')
        recurse(subreddit, hot_list, after, count + 1)
    return (hot_list)
