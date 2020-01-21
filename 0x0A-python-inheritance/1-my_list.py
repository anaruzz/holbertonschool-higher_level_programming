#!/usr/bin/python3
"""
Module that creates a class MyList that inherit from list
and prints it
"""
class MyList(list):
    """
    Class Mylist that inherits from list
    """
    def print_sorted(self):
        print(sorted(self))
