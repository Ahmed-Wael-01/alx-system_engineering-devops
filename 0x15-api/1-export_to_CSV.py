#!/usr/bin/python3
"""use api"""

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
        with open("{}.csv".format(empl_id), "w", newline="") as csvfile:
            for do in todo_list:
                csvfile.write('"{}","{}","{}","{}"\n'.format(
                    do['userId'], user.json()['name'],
                    do['completed'], do['title']))
    except Exception as e:
        print(e)
