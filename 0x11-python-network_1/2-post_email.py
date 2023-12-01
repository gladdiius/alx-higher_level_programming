#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys

if len(sys.argv) != 3:
    print("Usage: python script.py <URL>")
    sys.exit(1)
url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email})
data = data.encode('utf-8')

req = urllib.request.Request(url, data=data, method='POST')
with urllib.request.urlopen(req) as response:
    print(f'Your email is: {response.read().decode('utf-8')}')
