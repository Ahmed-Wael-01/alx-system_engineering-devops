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
                if do['completed'] is True:
                    todo_list.append(do)
                    done_c = done_c + 1
        print("Employee {} is done with tasks({}/{}):".format(
            user.json()['name'], done_c, full))
        for do in todo_list:
            print("\t {}".format(do['title']))
    except Exception as e:
        print(e)
