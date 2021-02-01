#!/usr/bin/python3
"""
module for task 1
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for i in users.json():
        if i.get('id') == int(argv[1]):
            USERNAME = (i.get('username'))
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for i in todos.json():
        if i.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((i.get('completed'), i.get('title')))
    filename = "{}.csv".format(argv[1])
    with open(filename, "w") as csvfile:
        f = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=f,
                                quoting=csv.QUOTE_ALL)
        for i in TASK_STATUS_TITLE:
            writer.writerow({"USER_ID": argv[1], "USERNAME": USERNAME,
                             "TASK_COMPLETED_STATUS": i[0],
                             "TASK_TITLE": i[1]})
