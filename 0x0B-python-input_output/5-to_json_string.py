#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """
    function that returns the JSON representation
    of an object
    @my_obj: object
    """
    return json.dumps(my_obj)
