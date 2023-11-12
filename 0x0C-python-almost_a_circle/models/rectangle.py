#!/usr/bin/python3
from models.base import Base
""" First Rectangle."""


class Rectangle(Base):
    """ class the inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ function that instantiate prive attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ function that gets width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """ function that sets value to width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ gets height value"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """setds the value to height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ gets value of x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """ sets value to x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ gets the value of y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """sets the value to y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """function that returns the area
        value of the Rectangle instance
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Function that prints in stdout the Rectangle
        instance with the character #
        """

    def display(self):
        """
        Function that prints in stdout the
        Rectangle instance with the character #
        """
        char = '#'
        for i in range(self.height):
            print(char * self.width)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))
