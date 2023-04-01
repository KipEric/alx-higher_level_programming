#!/usr/bin/python3
'''Python script that takes 2 arguments in order to list evaluates candidates applying for a back-end position'''

import requests
from sys import argv

if __name__ == "__main__":
    repository_name = argv[1]
    owner_name = argv[2]
    
    res = requests.get(url=f"https://api.github.com/repos/{owner_name}/{repository_name}/commits")
    commits = res.json()
    
    for commit in commits[:10]:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print(f"{sha}: {author}")
