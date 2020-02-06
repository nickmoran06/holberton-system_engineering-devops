#!/usr/bin/python3
"""

"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId=' + argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + argv[1]
    response_todos = requests.get(url_todos)
    response_user = requests.get(url_user)
    user = response_user.json()
    todos = response_todos.json()
    username = user.get('username')
    tasks = []
    json_obj = {}
    my_dict = {}
    filename = "{}.json".format(argv[1])

    for obj in todos:
        my_dict["task"] = obj.get('title')
        my_dict["completed"] = obj.get('completed')
        my_dict["username"] = username
        tasks.append(my_dict)

    json_obj[argv[1]] = tasks
    with open(filename, 'w') as json_file:
        json.dump(json_obj, json_file)
