#!/usr/bin/python3
"""
module for task 0
"""
import requests
from sys import argv


if __name__ == "__main__":
    TOTAL_NUM_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    for i in users.json():
        if i.get('id') == int(argv[1]):
            EMPLOYEE_NAME = (i.get('name'))
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for i in todos.json():
        if i.get('userId') == int(argv[1]):
            TOTAL_NUM_OF_TASKS += 1
            if i.get('completed') is True:
                    NUMBER_OF_DONE_TASKS += 1
                    TASK_TITLE.append(i.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))
    for i in TASK_TITLE:
        print("\t {}".format(i))
