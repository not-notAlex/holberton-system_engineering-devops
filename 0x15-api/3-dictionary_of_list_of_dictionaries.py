#!/usr/bin/python3
"""
module for task 3
"""
import json
import requests


if __name__ == "__main__":
    USERS = []
    use = requests.get("http://jsonplaceholder.typicode.com/users")
    for i in use.json():
        USERS.append((i.get('id'), i.get('username')))
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for i in todos.json():
        TASK_STATUS_TITLE.append((i.get('userId'),
                                  i.get('completed'),
                                  i.get('title')))
    data = dict()
    for i in USERS:
        tasks = []
        for j in TASK_STATUS_TITLE:
            if j[0] == i[0]:
                tasks.append({"task": j[2], "completed": j[1],
                              "username": i[1]})
        data[str(i[0])] = tasks
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(data, f, sort_keys=True)
