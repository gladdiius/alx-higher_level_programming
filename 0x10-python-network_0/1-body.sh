#!/bin/bash
# test
url=$1
response=$(curl -s -o /dev/null -w "%{http_code}" $url)

if [ $response -eq 200 ]; then
    curl -s $url
else
    echo "Non-200 status code: $response"
fi
