#!/usr/bin/python3

"""Square Model"""

from models.rectangle import Rectangle


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

    def update(self, *args, **kwargs):
        """A function that assigns key/value argument to square attributes"""

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)

            return

        try:

            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]

        except IndexError:
            pass

    def __str__(self):
        """ function that return
        [Square] (<id>) <x>/<y> - <size>
        """
        return (
            "[{}] ({}) {}/{} - {}".format(
                type(self).__name__, self.id, self.x, self.y, self.width
            )
        )

    def to_dictionary(self):
        """
        function that return the
        dictionary representation of a Rectangle
        """
        return ({
            'id': getattr(self, "id"),
            'x': getattr(self, "x"),
            'size': getattr(self, "width"),
            'y': getattr(self, "y")
            })
