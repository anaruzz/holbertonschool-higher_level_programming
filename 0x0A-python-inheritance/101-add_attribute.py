#!/usr/bin/python3
def add_attribute(obj=None, name="", value=""):
    """
    Function that adds a new attribute to an object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__setattr__(name, value)
