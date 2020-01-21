#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that inherited from a_class else False
    """
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
