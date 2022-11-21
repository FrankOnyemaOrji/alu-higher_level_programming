#!/usr/bin/python3
""" A Python script that:
- takes in a URL,
- sends a POST request to the passed URL with the email as a parameter,
- and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    res = sys.argv[1]
    req = requests.get(res)

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
