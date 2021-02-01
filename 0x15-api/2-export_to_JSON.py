#!/usr/bin/python3
"""
module for task 2
"""
from sys import argv
import json
import requests


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
    tasks = []
    for i in TASK_STATUS_TITLE:
        tasks.append({"task": i[1], "completed": i[0], "username": USERNAME})
    data = {str(argv[1]): tasks}
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as f:
        json.dump(data, f)
