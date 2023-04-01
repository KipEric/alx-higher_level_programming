#!/usr/bin/python3
'''Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).'''

import url.request
from sys import agrv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
