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


    @classmethod
    def save_to_file(cls, list_objs):
        """ save an object to a json file """
        with open(cls.__name__ + ".json", 'w') as f:
            if list_objs is None:
                s = "[]"
            else:
                s = cls.to_json_string([i.__dict__ for i in list_objs])
            f.write(s)
