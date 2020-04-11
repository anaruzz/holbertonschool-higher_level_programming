#!/bin/bash
# Displays the status code of a response from an HTTP request
curl -sI -o /dev/null -w "%{response_code}" "$1"
