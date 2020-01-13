#!/usr/bin/python3
"""
Modude that prints a square
size: size of square
"""
def print_square(size):
    """
    print square out of '#'
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
