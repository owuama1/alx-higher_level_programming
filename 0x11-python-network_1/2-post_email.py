#!/usr/bin/python3
"""
Sends a POST request to a URL with email param,
displays the body of the response in utf-8
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the data to be sent in the request body
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Create a POST request
    req = urllib.request.Request(url, data=data, method='POST')

    # Send the request and read the response
    with urllib.request.urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)
