#!/sur/bin/python3


"""
class Square that defines a square by: (based on 2-square.py)
Attribute:
    size
"""


class Square:
    """
    defined Square class
    """

    def __init__(self, size=0):
        """
        field instantiation
        """
        if not isinstance(size, int):
            """
            check if size is not integer
            """
            raise TypeError("size must be an integer")
        elif size < 0:
            """
            check if size is 0
            """
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        return the area of square
        """
        return (self.__size ** 2)
