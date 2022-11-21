#!/usr/bin/python3
""" A Python script that:
- takes in a URL,
- sends a request to the URL and displays the value of the variable
- X-Request-Id in the response header.
"""
import requests
import sys


if __name__ == "__main__":
    res = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {'q': res}

    req = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get('id'), response.get('name')))
    except ValueError:
        print("Not a valid JSON")
