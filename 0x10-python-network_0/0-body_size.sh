#!/bin/bash
# Use curl to send a request and display the size of the body in bytes
response_body_size=$('curl -sI "$1" | grep -i Content-Length')
echo "$response_body_size"

