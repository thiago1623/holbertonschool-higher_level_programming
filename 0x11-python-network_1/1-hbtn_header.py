#!/usr/bin/python3
"""
Grabs the header X-Request-Id from a url passed as an argument
"""
import urllib.request
import sys


if __name__ == '__main__':
    """request"""
    url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
