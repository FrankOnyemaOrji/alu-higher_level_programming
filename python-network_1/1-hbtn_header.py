#!/usr/bin/python3
"""Python script that takes in a URL,
-sends a request to the URL 
-and displays the body
 """
import sys
import urllib.request   
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode('ascii')

    res = urllib.request.Request(url, data)
    with urllib.request.urlopen(res) as response:
        print(response.read().decode('utf-8'))