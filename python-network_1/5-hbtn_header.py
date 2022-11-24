#!/usr/bin/python
"""Done with ducumenting"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    print("{}".format(res.headers.get("X-Request-Id")))