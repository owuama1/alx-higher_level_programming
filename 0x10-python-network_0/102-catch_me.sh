#!/bin/bash
# Sends a request to 0.0.0.0:5000/catch_me and retrieves the response containing "You got me!"
curl -s -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" "http://0.0.0.0:5000/catch_me"
