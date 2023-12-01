#!/usr/bin/python3
import requests
import sys

# Checking if username and personal access token are provided as command-line arguments
if len(sys.argv) != 3:
    print("Usage: ./10-my_github.py <username> <token>")
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

# Set the GitHub API endpoint for the authenticated user
url = "https://api.github.com/user"

# Set the authentication header with Basic Authentication using the personal access token
headers = {'Authorization': f'token {token}'}

# Sending a GET request to the GitHub API endpoint
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response as JSON
    user_data = response.json()
    
    # Display the user id
    print(user_data['id'])
else:
    # Display an error message if the request was not successful
    print(f"Error: {response.status_code}")

