#!/usr/bin/python3
"""
Task 9. Compare 2 Squares
"""


class Square:
    """
    class that define a square
    """

    @property
    def size(self):
        """  retrieve size """

        return (self__.size)

    @size.setter
    def size(self, value):
        """
        set size to value
        """

        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def __init__(self, size=0):
        """
        Instantiate size to size
        """

        self.__size = size

    def area(self):
        """
        return the current square area
        """

        return (self.__size ** 2)

    def __eq__(self, other):
        """
        compare if squares are equal
        """
        if isinstance(other, Square):
            return (self.area() == other.area())
        return (False)

    def __ne__(self, other):
        """
        compare if squares are not equal
        """
        if isinstance(other, Square):
            return not self.__eq__(other)

    def __gt__(self, other):
        """
        compares if  square are grater than
        """
        
        if isinstance(other, Square):
            return (self.area() > other.area())
        return (False)

    def __ge__(self, other):
        """
        check if squares are grater than or equal
        """
        if isinstance(other, Square):
            return (self.area() >= other.area())
        return (False)

    def __lt__(self, other):
        """
        compare if squares are less than
        """
        if isinstance(other, Square):
            return (self.area() < other.area())
        return (False)

    def __le__(self, other):
        """
        compare if Squares are less than or equal
        """
        if isinstance(other, Square):
            return (self.area() <= other.area())
        return (False)
