#!/usr/bin/python3
"""use api"""

import json
import requests
import sys


if __name__ == "__main__":
    try:
        todo_list = []
        empl_id = int(sys.argv[1])
        done_c = 0
        full = 0
        user = requests.get(
                "https://jsonplaceholder.typicode.com/users/{}".format(
                    empl_id))
        todos = requests.get("https://jsonplaceholder.typicode.com/todos")
        for do in todos.json():
            if empl_id == do['userId']:
                full = full + 1
                todo_list.append(do)
                done_c = done_c + 1
        with open("{}.json".format(empl_id), "w", newline="") as jfile:
            json.dump({empl_id: [{
                "task": t['title'],
                "completed": t['completed'],
                "username": user.json()['username']
            } for t in todos.json()]}, jfile)
    except Exception as e:
        print(e)
