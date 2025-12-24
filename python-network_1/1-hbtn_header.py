#!/usr/bin/python3
"""Fetches a URL and displays the value of the X-Request-Id header."""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        headers = response.headers
        print(headers.get("X-Request-Id"))
