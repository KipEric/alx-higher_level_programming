#!/usr/bin/python3
'''Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id'''

import requests
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]

    res = requests.get("https://api.github.com/user", auth=(username, password))

    if res.status_code == 200:
        user_data = res.json()
        print(f"User ID: {user_data['id']}")
    else:
        print("Error:", res.status_code)
