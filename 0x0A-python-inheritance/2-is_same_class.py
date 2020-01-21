#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    return True if obj is an instance of a_class else False
    """
    return issubclass(a_class, type(obj))
