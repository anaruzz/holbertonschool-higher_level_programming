#!/bin/bash
# Script that sends delete request and display body of response
curl -sI $1 | grep Allow | cut -d ' ' -f2-
