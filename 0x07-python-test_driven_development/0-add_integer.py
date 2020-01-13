#!/usr/bin/python3
"""
Module returns the addition of two numbers (int)
a : integer or float to add
b : integer or float to add
"""


def add_integer(a, b=98):
    """
    Returns a + b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
