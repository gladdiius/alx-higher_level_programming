#!/usr/bin/python3
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print(f"Body response:\n\t- type: {type(body)}\n\t- content: {body.decode('utf-8')}")
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
except urllib.error.URLError as e:
    print(f"Error: {e.reason}")

