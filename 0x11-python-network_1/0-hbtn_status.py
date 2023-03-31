#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''
from urllib import request

if __name__=="__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        content = response.read()
        print("Body responses:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
