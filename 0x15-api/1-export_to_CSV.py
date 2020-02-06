#!/usr/bin/python3
"""
Script that use an API to show and get information about employee with CSV
"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    user = requests.get("https://jsonplaceholder.typicode.com/users/{userID}".
                        format(userID=argv[1])).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(argv[1])).json()

    with open("{userID}.csv".format(userID=argv[1]), 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for obj in todo:
            writer.writerow([int(argv[1]), user.get('username'),
                             obj.get('completed'), obj.get('title')])
