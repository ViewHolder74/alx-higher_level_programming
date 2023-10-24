#!/usr/bin/python3


"""
class Square that defines a square by: (based on 1-square.py)
Atrribute:
    size
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """ Instantiation with optional """
        if not isinstance(size, int):
            """
            check if size is interger
            """
            raise TypeError("size must be an integer")
        elif size < 0:
            """
            check if size is less than 0
            """
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
