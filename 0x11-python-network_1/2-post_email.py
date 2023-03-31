#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST 
request to the passed URL with the email as a parameter, and displays the body of the response"""
import urllib.request
from sys import argv

if __name__ == "__main__":
    value = {'email': argv[2]}
    content = urllib.parse.urlencode(value).encode('ascii')
    res = urllib.request.Request(argv[1], data=content, method='POST')
    with urllib.request.urlopen(res) as r:
        read = r.read().decode('utf-8')
        print(read)
