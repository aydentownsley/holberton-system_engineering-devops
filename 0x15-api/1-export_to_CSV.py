#!/usr/bin/python3
""" Exports info to CSV """
import csv
import json
import sys
from urllib import request


if __name__ == "__main__":

    tasks = 0
    tasks_comp = 0

    req = request.Request('https://jsonplaceholder.typicode.com/todos')
    req_user = request.Request('https://jsonplaceholder.typicode.com/users')

    with request.urlopen(req_user) as resu:
        data = json.loads(resu.read().decode('utf-8'))
        for k in data:
            if k.get('id') == int(sys.argv[1]):
                name = k['username']

    with request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        with open('{}.csv'.format(sys.argv[1]), mode='w') as file:
            write = csv.writer(file, quoting=csv.QUOTE_ALL)
            for x in data:
                if x.get('userId') == int(sys.argv[1]):
                        write.writerow([sys.argv[1], name,
                                       x.get('completed'), x.get('title')])
