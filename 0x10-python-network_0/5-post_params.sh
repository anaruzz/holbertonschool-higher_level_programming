#!/bin/bash
# Script that sends delete request and display body of response
curl -sX POST "$1" -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
