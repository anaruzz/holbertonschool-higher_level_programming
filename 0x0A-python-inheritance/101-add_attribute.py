#!/usr/bin/python3
def add_attribute(obj=None, name="", value=""):
    """
    Function that adds a new attribute to an object
    """
    try:
        obj.__setattr__(name, value)
    except Exception as e:
        raise TypeError("can't add new attribute")
