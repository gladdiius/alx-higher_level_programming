#!/bin/bash
# This script takes a URL as an argument, sends a DELETE request to that URL using curl, and displays the body of the response
curl -X DELETE -s $1
