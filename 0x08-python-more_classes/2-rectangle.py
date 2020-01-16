#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        if height is not None:
            if type(height) is not int:
                raise TypeError('height must be integer')
            if height < 0:
                raise ValueError('height must be >= 0')
            self.__height = height
        if width is not None:
            if type(width) is not int:
                raise TypeError('width must be integer')
            if width < 0:
                raise ValueError('width must be >= 0')
            self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
