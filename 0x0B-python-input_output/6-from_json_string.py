#!/usr/bin/python3
import json


def from_json_string(my_str):
    """
    function that returns obj from JSON representation
    @my_str: json string
    """
    return json.loads(my_str)
