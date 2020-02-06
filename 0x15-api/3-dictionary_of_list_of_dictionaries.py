#!/usr/bin/python3
"""
Script that use an API to show and get information about employee
"""

import json
import requests

if __name__ == '__main__':
    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    user_dict = {}
    username_dict = {}
    for user in users:
        user_id = user.get("id")
        user_dict[user_id] = []
        username_dict[user_id] = user.get("username")

    for task in todos:
        task_dict = {}
        user_id = task.get("userId")
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username_dict.get(user_id)
        user_dict.get(user_id).append(task_dict)

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(user_dict, json_file)
