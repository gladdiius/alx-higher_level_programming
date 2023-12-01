#!/usr/bin/python3
import urllib.request

def fetch_status(url):
    """
    Fetches the status from the given URL using the urllib package.

    :param url: The URL to fetch the status from.
    :type url: str
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(f"Body response:\n\t- type: {type(body)}\n\t- content: {body.decode('utf-8')}")
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")

if __name__ == "__main__":
    # Example usage:
    url = "https://alx-intranet.hbtn.io/status"
    fetch_status(url)

