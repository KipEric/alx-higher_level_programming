#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL 
and displays the value of the X-Request-Id variable found in the header of the response."""

import urllib.request
from sys import argv

with urllib.request.urlopen(argv[1]) as id:
    info = id.info()
    content = info.get('X-Request-Id')
    print(content)