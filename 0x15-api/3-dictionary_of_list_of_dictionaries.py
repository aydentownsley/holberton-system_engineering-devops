#!/usr/bin/python3
""" Exports info to CSV """
import json
from urllib import request


if __name__ == "__main__":

    dict_to_json = {}
    list_of_dict = []
    names = []
    i = 1

    req = request.Request('https://jsonplaceholder.typicode.com/todos')
    req_user = request.Request('https://jsonplaceholder.typicode.com/users')

    with request.urlopen(req_user) as resu:
        data = json.loads(resu.read().decode('utf-8'))
        for k in data:
            names.append(k.get('username'))

    with request.urlopen(req) as res:
        data = json.loads(res.read().decode('utf-8'))
        for i in range(1, 10):
            list_of_dict = []
            for k in data:
                if k.get('userId') == i:
                    list_of_dict.append({"username": names[i - 1],
                                        "task": k.get('title'),
                                        "completed": k.get('completed')})
                dict_to_json[i] = list_of_dict
        with open('todo_all_employees.json', 'w') as file:
            json.dump(dict_to_json, file)
