#!/usr/bin/python3
"""
Uses the GitHub API to display the user's id using
Basic Authentication with a personal access token.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    # Create the Basic Authentication credentials
    auth = (username, token)

    # Send the GET request to the GitHub API
    response = requests.get('https://api.github.com/user', auth=auth)

    try:
        # Parse the response as JSON
        response_json = response.json()
        # Display the user's id
        print(response_json.get('id'))
    except ValueError:
        # If the response is not a valid JSON, handle the error
        print("Not a valid JSON")
