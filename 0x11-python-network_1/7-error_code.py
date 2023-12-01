#!/usr/bin/python3
import requests
import sys

# Checking if a URL is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: ./7-error_code.py <URL>")
    sys.exit(1)

url = sys.argv[1]

# Sending a GET request to the specified URL using requests
response = requests.get(url)

# Displaying the body of the response
print(response.text)

# Checking the HTTP status code
if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
