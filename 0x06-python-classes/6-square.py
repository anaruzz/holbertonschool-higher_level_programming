#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if size is not None:
            if type(size) is not int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        message = 'position must be a tuple of 2 positive integers'
        if position is not None:
            if type(position) is not tuple:
                raise TypeError(message)
            elif len(position) != 2:
                raise TypeError(message)
            elif type(position[0]) is not int and type(position[1]) is not int:
                raise TypeError(message)
            elif position[0] < 0 or position[1] < 0:
                raise TypeError(message)
            else:
                self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(' ', end="")
                for k in range(self.__size):
                    print('#',  end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int and type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
