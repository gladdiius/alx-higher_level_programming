#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

with urllib.request.urlopen(url, data=data) as response:
    # Reading and decoding the body of the response
    body = response.read().decode('utf-8')
    print(body)
