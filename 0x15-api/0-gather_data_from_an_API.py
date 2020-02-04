#!/usr/bin/python3
"""
Script that use an API to show and get information about employee
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    name_request = requests.get(url + "/users/" + argv[1]).json().get('name')
    todo_request = requests.get(url + '/todos?userId=' + argv[1]).json()
    completed_list = []

    for obj in todo_request:
        if obj.get('completed') is True:
            completed_list.append(obj)

    print("Employee {} is done with tasks".format(name_request), end="")
    print("({}/{}):".format(len(completed_list), len(todo_request)))
    for obj in completed_list:
        print("\t {}".format(obj.get("title")))
