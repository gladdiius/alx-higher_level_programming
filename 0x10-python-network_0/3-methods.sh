#!/bin/bash
# Check if the URL argument is provided
curl -s -X OPTIONS -i $1 | grep "Allow:" | cut -d ' ' -f 2-
