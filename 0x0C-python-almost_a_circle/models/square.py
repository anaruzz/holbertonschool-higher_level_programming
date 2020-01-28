#!/usr/bin/python3
"""Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ constructor for  class Square """
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ String representation11"""
        i = self.id
        x = self.x
        y = self.y
        s = self.size
        return ("[Square] ({}) {}/{} - {}".format(i, x, y, s))

    @property
    def size(self):
        """ property setter for size attribute"""
        return Rectangle.__width

    @size.setter
    def size(self, width):
        """ propety setter for size attribute"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        Rectangle.__width = width
        Rectangle.__height = width

    def update(self, *args, **kwargs):
        """ Update the attributes with args and kwars"""
        x = len(args)
        if x == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
            return
        else:
            if x >= 1:
                self.id = args[0]
            if x >= 2:
                self.size = args[1]
            if x >= 3:
                self.x = args[2]
            if x >= 4:
                self.y = args[3]
            return

    def to_dictionary(self):
         dic = {'id' : self.id,
                'size' : self.size,
                'x' : self.x,
                'y' : self.y}
        return dic
