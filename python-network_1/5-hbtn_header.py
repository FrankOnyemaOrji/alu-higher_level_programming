#!/usr/bin/python3
""" A Python script that:
- takes in a URL,
- sends a request to the URL and displays the value of the variable
- X-Request-Id in the response header.
"""
import requests
import sys


if __name__ == "__main__":
    res = sys.argv[1]

    req = requests.get(res)
    print(req.headers.get('X-Request-Id'))
