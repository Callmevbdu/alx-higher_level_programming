#!/usr/bin/python3

import urllib.parse
import urllib.request
import sys


"""
a Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8).
"""

if __name__ == "__main__":
    url, email = sys.argv[1:]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print(body)
