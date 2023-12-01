#!/usr/bin/python3
import requests
import sys

# Checking if repository name and owner name are provided as command-line arguments
if len(sys.argv) != 3:
    print("Usage: ./10-commits.py <repository_name> <owner_name>")
    sys.exit(1)

repository_name = sys.argv[1]
owner_name = sys.argv[2]

# Set the GitHub API endpoint for listing commits
url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

# Set the parameters to get the most recent 10 commits
params = {'per_page': 10}

# Sending a GET request to the GitHub API endpoint
response = requests.get(url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response as JSON
    commits = response.json()
    
    # Display the 10 most recent commits
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
else:
    # Display an error message if the request was not successful
    print(f"Error: {response.status_code}")
