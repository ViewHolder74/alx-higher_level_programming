#!/usr/bin/python3
from models.rectangle import Rectangle
""" Square Class."""


class Square(Rectangle):
    """ class that inherits from Rectangle:"""

    def __init__(self, size, x=0, y=0, id=None):
        """Function that instantiate attribues"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get width."""
        return (self.width)

    @size.setter
    def size(self, value):
        """ sets value to width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """ function that return
        [Square] (<id>) <x>/<y> - <size>
        """
        return("[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
            self.x, self.y, self.width))

