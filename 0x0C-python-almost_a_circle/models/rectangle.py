#!/usr/bin/python3

"""Rectangle Model"""

from models.base import Base


class Rectangle(Base):
    """ class the inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ function that instantiate prive attributes"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        print('\n' * self.y, end='')
        for _ in range(self.height):
            print(' ' * self.x + char * self.width)

    def __str__(self):
        """
        Function that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<heigh>
        """
        return (
            "[{}] ({}) {}/{} - {}/{}".format(
                type(self).__name__, self.id, self.x, self.y,
                self.width, self.height
            )
        )

    def update(self, *args, **kwargs):
        """
        Function  that assigns an
        argument to each attribute.
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]

        except IndexError:
            pass

    def to_dictionary(self):
        """ return dict repr."""
        return ({
            'x': getattr(self, "x"),
            'y': getattr(self, "y"),
            'id': getattr(self, "id"),
            'height': getattr(self, "height"),
            'width': getattr(self, "width")
        })
