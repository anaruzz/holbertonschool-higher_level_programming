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
        """ Save to json string file"""
        with open(cls.__name__ + ".json", 'w') as f:
            s = []
            if list_objs is not None:
                for i in list_objs:
                    s.append(i.to_dictionary())
            f.write(cls.to_json_string(s))

    @staticmethod
    def from_json_string(json_string):
        s = []
        if json_string is None:
            return s
        else:
            s = json.loads(json_string)
            return s

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        s = []
        with open(cls.__name__ + ".json", 'r') as f:
            not_empty = f.read()
            if not not_empty:
                return cls.from_json_string(s)
            list_inst = cls.from_json_string(not_empty)
            for i in list_inst:
                s.append(cls.create(**i))
        return s
