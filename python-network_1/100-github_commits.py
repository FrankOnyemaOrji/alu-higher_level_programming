#!/usr/bin/python3
""" list the 10 most recents commits on a given GitHub respository"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],)

    req = requests.get(url)
    commits = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get('sha'), commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
    