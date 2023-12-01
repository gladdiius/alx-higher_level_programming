#!/usr/bin/python3
import requests
import sys

# Checking if a URL and email are provided as command-line arguments
if len(sys.argv) != 3:
    print("Usage: ./6-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Sending a POST request to the specified URL using requests
response = requests.post(url, data={'email': email})

# Displaying the body of the response
print(response.text)
