#!/usr/bin/python3
if __name__ == "__main__":
    BaseGeometry = __import__('abc').BaseGeometry
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
        self.__width = width
        self.__height = height
