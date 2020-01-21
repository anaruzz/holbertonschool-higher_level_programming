#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    return True if type of obj is a subclass of a_class else False
    """
    return issubclass(a_class, type(obj))
