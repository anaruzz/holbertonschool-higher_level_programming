#!/usr/bin/python3
from models.base import *
""" rectangle"""


class Rectangle(Base):
    """
    class Rectangle that inherits from class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        property getter for width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        property setter for width attribute
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        property getter for height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        property setter for height attribute
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        property getter for x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        property setter for x attribute
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        property getter for y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        property setter for y attribute
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        return area value of a rectangle
        """
        return self.height * self.width

    def display(self):
        """
        display a rectangle in "#"
        """
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """
        string representation of instance
        """
        i = str(self.id)
        x = str(self.x)
        y = str(self.y)
        w = str(self.width)
        h = str(self.height)
        a = "[Rectangle] (" + i + ") " + x + "/" + y + "-" + w + "/" + h
        return a

    def update(self, *args, **kwargs):
            x = len(args)
            if x == 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    if key == "width":
                        self.width = value
                    if key == "height":
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value
                return
            else:
                if x >= 1:
                    self.id = args[0]
                if x >= 2:
                    self.width = args[1]
                if x >= 3:
                    self.height = args[2]
                if x >= 4:
                    self.x = args[3]
                if x >= 5:
                    self.y = args[4]
                return
