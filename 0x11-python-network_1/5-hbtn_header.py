#!/usr/bin/python3
import requests
import sys

# Checking if a URL is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: ./5-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

# Sending a GET request to the specified URL using requests
response = requests.get(url)

# Retrieving the value of the X-Request-Id from the response headers
x_request_id = response.headers.get('X-Request-Id')

# Displaying the value of X-Request-Id
if x_request_id:
    print(x_request_id)
else:
    print("X-Request-Id not found in the response headers.")

