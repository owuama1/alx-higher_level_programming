#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with letter as a param
Handles various response cases and prints the result.
"""
import requests
import sys

if __name__ == "__main__":
    # Set q to the first argument or an empty string if no argument is given
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Create the payload with the letter
    data = {'q': q}

    # Send the POST request
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        # Try to parse the response as JSON
        response_json = response.json()

        if response_json:
            # If JSON is not empty, display id and name
            print("[{}] {}".format(response_json.get('id'),
                  response_json.get('name')))
        else:
            # If JSON is empty, display 'No result'
            print("No result")
    except ValueError:
        # If JSON is invalid, display 'Not a valid JSON'
        print("Not a valid JSON")
