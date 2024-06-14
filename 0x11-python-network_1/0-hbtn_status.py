#!/usr/bin/python3
"""
Fetches the status from https://alx-intranet.hbtn.io/status
Displays the body of the response in a formatted manner.
"""
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print(f"Body response:")
        print(f"\t- type: {type(body).__name__}")
        print(f"\t- content: {body.decode('utf-8')}")
