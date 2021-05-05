#!/usr/bin/python3
""" Exports info to CSV """
import csv
import json
import sys
from urllib import request


if __name__ == "__main__":

    dict_to_json = {}
    task_dict = {}
    task_list = []

    req = request.Request('https://jsonplaceholder.typicode.com/todos')
    req_user = request.Request('https://jsonplaceholder.typicode.com/users')

    with request.urlopen(req_user) as resu:
        data = json.loads(resu.read().decode('utf-8'))
        for k in data:
            if k.get('id') == int(sys.argv[1]):
                name = k['username']

    with request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for x in data:
            if x.get('userId') == int(sys.argv[1]):
                task_list.append({"task": x.get('title'),
                                  "completed": x.get('completed'),
                                  "username": name})

    dict_to_json[sys.argv[1]] = task_list
    json_dump = json.dumps(dict_to_json)
    print(json_dump)
