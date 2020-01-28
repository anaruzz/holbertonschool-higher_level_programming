#!/usr/bin/python3
""" base Module is the parent of all shapes"""
import json


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
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return json representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        s = []
        if list_objs is None:
            f.write(s)
        else:
            with open(cls.__name__ + ".json", 'w') as f:
                for obj in list_objs:
                    s += to_json_string(obj)
                f.write(s)
