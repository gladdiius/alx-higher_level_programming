#!/usr/bin/python3
import urllib.request
import sys
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)
url = sys.argv[1]

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    print(response.headers.get('X-Request-Id'))
