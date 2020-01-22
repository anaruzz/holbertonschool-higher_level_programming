#!/usr/bin/python3


import json
from sys import argv
from os import stat  # to check if file is empty
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'
no_file = 0
try:
    with open(filename, encoding='UTF-8') as f:
        f.read()
except FileNotFoundError:
    no_file = 1

if no_file or stat(filename).st_size == 0:
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write('[]')
args = load_from_json_file(filename)
for arg in argv[1:]:
    args.append(arg)
save_to_json_file(args, filename)
