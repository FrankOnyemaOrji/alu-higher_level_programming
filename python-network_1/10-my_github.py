#!/usr/bin/python3
""" A Python script that:
- takes in a URL,
- sends a request to the URL and displays the value of the variable
- X-Request-Id in the response header.
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get('https://api.github.com/user', auth=auth)
    print(req.json().get('id'))
