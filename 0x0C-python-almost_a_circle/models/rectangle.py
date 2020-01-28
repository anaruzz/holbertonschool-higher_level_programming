#!/usr/bin/python3

""" Rectangle Class Module"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class, inherits from Base """

    def __str__(self):
        """ String representation of a Rectangle """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
                self.id, self.x, self.y, self.width, self.height)

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns private instance attribute """
        return self.__width

    @width.setter
    def width(self, val):
        """ sets private instance attribute """
        if type(val) is not int:
            raise TypeError('width must be an integer')
        if val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val

    @property
    def height(self):
        """ returns private instance attribute """
        return self.__height

    @height.setter
    def height(self, val):
        """ sets private instance attribute """
        if type(val) is not int:
            raise TypeError('height must be an integer')
        if val <= 0:
            raise ValueError('height must be > 0')
        self.__height = val

    @property
    def x(self):
        """ returns private instance attribute """
        return self.__x

    @x.setter
    def x(self, val):
        """ sets private instance attribute """
        if type(val) is not int:
            raise TypeError('x must be an integer')
        if val < 0:
            raise ValueError('x must be >= 0')
        self.__x = val

    @property
    def y(self):
        """ returns private instance attribute """
        return self.__y

    @y.setter
    def y(self, val):
        """ sets private instance attribute """
        if type(val) is not int:
            raise TypeError('y must be an integer')
        if val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val

    def area(self):
        """ returns the area value of a Rectangle object """
        return self.width * self.height

    def display(self):
        """ display a rectangle in "#" """
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """string representation of instance """
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
