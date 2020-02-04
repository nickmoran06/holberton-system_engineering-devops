#!/usr/bin/python3
"""
Script that use an API to show and get information about employee with CSV
"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    name_request = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + argv[1]
    ).json()
    todo_request = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    ).json()

    with open("{userID}.csv".format(userID=argv[1]), 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for obj in todo_request:
            writer.writerow([
                int(argv[1]),
                name_request.get('username'),
                obj.get('completed'),
                obj.get('title')
            ])
