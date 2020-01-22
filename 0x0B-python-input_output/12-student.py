#!/usr/bin/python3
class Student:
    """
    class student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        selected_a = {}
        for existing_a, value in self.__dict__.items():
            for requested_a in attrs:
                if requested_a is existing_a:
                    selected_a[existing_a] = value
        return selected_a
