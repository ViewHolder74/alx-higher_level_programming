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
            """ get width value"""
            return (self.__width)

        @width.setter
        def width(self, width):
            """ sets width"""
            self.__width = width

        @property
        def height(self):
            """ gets height value"""
            return (self.__height)

        @height.setter
        def height(self, height):
            """setds the value to height"""
            self.__height = height

        @property
        def x(self):
            """ gets value of x"""
            return (self.__x)

        @x.setter
        def x(self, x):
            """ sets value to x"""
            self__.x = x

        @property
        def y(self):
            """ gets the value of y"""
            return (self.__y)

        @y.setter
        def y(self, y):
            """sets the value to y"""
            self.__y = y
