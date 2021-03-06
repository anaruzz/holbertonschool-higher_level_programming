#!/usr/bin/python3
def add_attribute(obj, name, value):
    """
    Function that adds a new attribute to an object
    """
    if type(obj) in [str, int, float, complex, bool, set, tuple, list]:
        raise TypeError("can't add new attribute")
    else:
        obj.name = value
