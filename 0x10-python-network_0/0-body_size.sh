#!/bin/bash
# display length of content of body of response
curl -sI $1 | grep Content-Length | cut -d ' ' -f2
