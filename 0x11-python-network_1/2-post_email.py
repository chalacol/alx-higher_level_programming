#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url_passed = sys.argv[1]
    email_passed = {'email': sys.argv[2] }
    data = urllib.parse.urlencode(email_passed).encode("ascii")

    request = urllib.request.Request(url_passed, data) 
    with urllib.request.urlopen(url_passed) as req:
        print(req.read().decode('utf-8'))
