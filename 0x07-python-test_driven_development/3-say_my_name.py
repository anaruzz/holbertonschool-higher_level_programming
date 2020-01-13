#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if type(first_name) is not string:
        raise TypeError('first name must be a string')
    if type(last_name) is not string:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
