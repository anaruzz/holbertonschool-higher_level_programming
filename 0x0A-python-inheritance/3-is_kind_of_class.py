#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    return True if obj is instance of a_class or of a class that it inherits from
    """
    return isinstance(obj, a_class)
