#!/bin/bash
# This is a bash script that takes in a URL, send a GET request to an
# URL with curl, and display the body of the response
curl -sL "$1"
