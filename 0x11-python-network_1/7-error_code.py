#!/usr/bin/python3
import requests
import sys
if len(sys.argv) != 2:
    print("Usage: ./7-error_code.py <URL>")
    sys.exit(1)
url = sys.argv[1]
response = requests.get(url)
if response.status_code >= 400:
    print(f"Error code: {response.status_code}")
