#!/usr/bin/python3

import urllib.request
import sys


"""
a Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8).
"""

if __name__ == "__main__":
    url = sys.argv[1:]

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
