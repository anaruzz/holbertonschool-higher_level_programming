#!/usr/bin/python3
class MyInt(int):
    """
    class MyInt that inherits from class int
    but reverses the == and != operators
    """
    def __init__(self, data):
        """
        initialize the data
        @data: value of the object
        """
        if isinstance(data, int):
            self.__data = data

    def __eq__(self, value):
        """
        Treat == as !=
        @value: value to compare self with
        """
        return self.__data != value

    def __ne__(self, value):
        """
        treat != as ==
        @value: value to compare self with
        """
        return self.__data == value
