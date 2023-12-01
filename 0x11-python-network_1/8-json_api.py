#!/usr/bin/python3
import requests
import sys

# Set the URL for the POST request
url = "http://0.0.0.0:5000/search_user"

# Set the parameter 'q' to the provided letter or an empty string if not provided
q = sys.argv[1] if len(sys.argv) > 1 else ""

# Sending a POST request to the specified URL using requests
response = requests.post(url, data={'q': q})

try:
    # Try to parse the response as JSON
    json_data = response.json()

    # Check if the JSON is properly formatted and not empty
    if json_data:
        print(f"[{json_data['id']}] {json_data['name']}")
    else:
        print("No result")

except ValueError:
    # Handle the case where the response is not a valid JSON
    print("Not a valid JSON")

