#!/usr/bin/python3

"""
Task 2: Area and Perimeter.
"""


class Rectangle:
    """ class that defines a rectangle """

    @property
    def width(self):
        """ function that gets width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ function that sets width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ function that gets height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ function that sets height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """ Instatiate private attribute """
        self.__width = width
        self.__height = height

    def area(self):
        """ calculate are of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ claculate perimeter of rectangle """
        if self.__width != 0:
            a = self.__width * 2
        if self.__height != 0:
            b = self.__height * 2
        return (a + b)
