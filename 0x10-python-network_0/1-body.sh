#!/bin/bash
# Send a GET request to the URL and display the body of the response for status code 200
response=$(curl -s -o /dev/null -w "%{http_code}" $1)
if [ $response -eq 200 ]; then
  curl -s $1
fi
