
Skip to content
Pull requests
Issues
Marketplace
Explore
@anaruzz
Code Issues 0 Pull requests 0 Projects 0 Wiki Security Pulse Community
holbertonschool-higher_level_programming/0x08-python-more_classes/1-rectangle.py /
@MatriMariem MatriMariem check order of output 8ffed36 11 hours ago
executable file 40 lines (34 sloc) 978 Bytes
You're using code navigation to jump to definitions or references.
Learn more or give us feedback
#!/usr/bin/python3
"""
module contains one class
"""


class Rectangle:
    """ class Rectangle """
    def __init__(self, width=0, height=0):
        """ instantiation """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @width.setter
    def width(self, value):
        """ setter for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
