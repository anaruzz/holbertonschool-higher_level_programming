#!/usr/bin/python3
""" base Module is the parent of all shapes"""


class Base:
    """
    The base of all other classes in the project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        @id: the id of every object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
