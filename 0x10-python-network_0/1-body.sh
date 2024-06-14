#!/bin/bash
# Sends a GET request to a URL and displays the body of the response only if the status code is 200
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"
