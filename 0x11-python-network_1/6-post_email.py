#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter
and displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email parameter
    data = {'email': email}

    # Send the POST request
    response = requests.post(url, data=data)

    # Print the body of the response
    print(response.text)
