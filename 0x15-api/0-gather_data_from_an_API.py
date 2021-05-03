#!/usr/bin/python3
""" Grabs info from API """
import json
import sys
from urllib import request


if __name__ == "__main__":

    tasks = 0
    tasks_comp = 0
    req = request.Request('https://jsonplaceholder.typicode.com/todos')
    req_user = request.Request('https://jsonplaceholder.typicode.com/users')

    with request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for x in data:
            if x.get('userId') == int(sys.argv[1]):
                tasks += 1
                if x.get('completed') is True:
                    tasks_comp += 1

    with request.urlopen(req_user) as resu:
        data = json.loads(resu.read().decode('utf-8'))
        for k in data:
            if k.get('id') == int(sys.argv[1]):
                name = k['name']

    print('Employee {} is done with tasks({}/{}):'.format(name,
          tasks_comp, tasks))

    with request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for x in data:
            if x.get('userId') == int(sys.argv[1]):
                if x.get('completed') is True:
                    print('\t {}'.format(x['title']))
