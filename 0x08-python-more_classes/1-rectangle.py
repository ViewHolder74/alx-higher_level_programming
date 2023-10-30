#!/usr/bin/python3
"""Task 1, Real definition of a rectangle."""


class Rectangle:
    """class that defines a rectangle"""

    @property
    def width(self):
        """returning width value"""
        
        return (self.__width)

    @width.setter
    def width(self, value):
        """assigning with a value."""
        
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
            
        if value < 0:
            raise ValueError("width must be >= 0")
            
        self.__width = value

    @property
    def height(self):
        """Returning hieght"""
        
        return (self.__height)

    @height.setter
    def height(self, value):
        """setting width to value"""
        
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
            
        if value < 0:
            raise ValueError("height must be >= 0")
            
        self.__height = value

    def __init__(self, width=0, height=0):
        """instantiating private attribute"""
        
        self.__width = width
        self.__height = height
