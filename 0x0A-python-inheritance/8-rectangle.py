#!/usr/bin/python3
class BaseGeometry:
    """
    class named BaseGeometry
    """
    def area(self):
        """
        raise an exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        validates if a value of a name is integer and greater than 0
        returns nothing
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

class Rectangle(BaseGeometry):
    """
    creates a class calles Rectangle tht inherits from class BaseGeometry
    """
    def __init__(self, width, height):
        """
        initialize an object of Rectangle with
        @width: width of rectangle
        @height: height of rectangle
        """
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)
