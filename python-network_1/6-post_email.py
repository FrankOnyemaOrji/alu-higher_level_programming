#!/usr/bin/python3
"""Documented with a module"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = sys.argv[2]
    res = requests.post(url, data={"email": res})
    print("{}".format(res.text))
