#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an object to a text file
    @my_obj: object
    @filename: the name of the file
    """
    with open(filename, mode="w", encoding='UTF-8') as f:
        f.write(json.dumps(my_obj))
