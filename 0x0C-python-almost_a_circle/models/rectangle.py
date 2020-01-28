#!/usr/bin/python3
""" Rectangle Module """

from models.base import Base


class Rectangle(Base):
    """ class Rectangle is a Base yeld """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle constructor """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return(self.__width)

    @width.setter
    def width(self, width):
        """ width setter """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """ height getter """
        return(self.__height)

    @height.setter
    def height(self, height):
        """ height setter """
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """ x getter """
        return(self.__x)

    @x.setter
    def x(self, x):
        """ x setter """
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """ y getter """
        return(self.__y)

    @y.setter
    def y(self, y):
        """ y setter """
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """ rectangle area """
        return (self.height*self.width)

    def display(self):
        """ draw rectangle with '#' """
        print("\n"*self.y, end='')
        for i in range(0, self.height):
            print(" "*self.x, end='')
            for j in range(0, self.width):
                print("#", end='')
            print()

    def __str__(self):
        """ returns a string that defines the rectangle """
        return("[Rectangle] (" + str(self.id) + ") " +
               str(self.x)+"/"+str(self.y)+" - " +
               str(self.width)+"/"+str(self.height))

    def update(self, *args, **kwargs):
        """ update rectangle with new values """
        i = 0
        attr = ['id', 'width', 'height', 'x', 'y']
        kw = list(set(kwargs.keys()))
        for k in args:
            if k:
                exec("self.%s = %d" % (attr[i], k))
            i += 1
        for k in kw:
            exec("self.%s = %d" % (k, kwargs[k]))
