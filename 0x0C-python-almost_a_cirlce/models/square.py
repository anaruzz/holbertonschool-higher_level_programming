#!/usr/bin/python3
from models.rectangle import *

"""Square"""
class Square(Rectangle):
    """
    Class Square that inherits from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
         super().__init__(size, size, x, y, id)
         self.size = size

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size))
