#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """
    function that creates object from json file
    @filename: the name of the file
    """
    with open(filename, encoding='UTF-8') as f:
        obj = json.load(f)
        return obj
