#!/bin/bash
# This is a bash script that send a DELETE request to an URL with curl
# and display the body of the response
curl -sX DELETE "$1"
