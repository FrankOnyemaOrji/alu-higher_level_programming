#!/usr/bin/python3
"""Python script that takes in a URL,
-sends a request to the URL 
-and displays the body
"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html["X-Request-Id"])
