#!/usr/bin/python3
import json
def to_json_string(my_obj):
    """
    function that appends a text to a file
    @filename: the path of the file
    @text: text to be added
    """
    return json.dumps(my_obj)
