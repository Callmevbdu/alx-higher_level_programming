#!/bin/bash
# a Bash script that takes in a URL and displays all HTTP methods the server
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
