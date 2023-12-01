#!/usr/bin/python3
import requests
import sys

# Setting the default value for q if no argument is given
q = sys.argv[1] if len(sys.argv) > 1 else ""

# Sending a POST request to the specified URL using requests
response = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})

try:
    # Parsing the response as JSON
    result = response.json()

    # Checking if the JSON is properly formatted and not empty
    if result:
        print(f"[{result['id']}] {result['name']}")
    else:
        print("No result")

except ValueError:
    # Handling invalid JSON
    print("Not a valid JSON")
