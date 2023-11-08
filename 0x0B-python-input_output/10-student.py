#!/usr/bin/python3
""" Task 10: Student to JSON with filter """


class Student:
    """ class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """ Function that instantiate attributes."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Function that retrieves a dictionary representation
        of Student instance."""

        if (type(attrs) == list and all(type(i) == str for i in attrs)):
            return ({j: getattr(self, j) for j in attrs if hasattr(self, j)})

        return (self.__dict__)
