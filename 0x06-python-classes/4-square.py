#!/usr/bin/python3
"""
Task 4.
Acess and update private attribute
"""



class Square:
    """
    class that defines a square
    """

    @property
    def size(self):
        """ private instance attribute: size """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        set size to value
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def __init__(self, size=0):
        """ Instantiate size """

        self.__size = size

    def area(self):
        """ calcluate area of a square """

        return (self.__size ** 2)
