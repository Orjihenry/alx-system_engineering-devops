#!/usr/bin/python3
""" Script that exports data in JSON format. """
import json
import requests as req
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = req.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = req.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
