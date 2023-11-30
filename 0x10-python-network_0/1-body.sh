#!/bin/bash
# This script takes a URL as an argument, sends a GET request to that URL using curl, and displays the body of the response if the status code is 200

# Check if the URL argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a GET request to the URL and display the body of the response for status code 200
response=$(curl -s -o /dev/null -w "%{http_code}" $1)
if [ $response -eq 200 ]; then
  curl -s $1
fi
