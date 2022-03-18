#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        read_res = res.read()
        print("Body response:")
        print('\t - type: {}'.format(type(read_res)))
        print('\t - content: {}'.format(read_res))
        print('\t - utf8 content: {}'.format(read_res.decode('utf-8')))
