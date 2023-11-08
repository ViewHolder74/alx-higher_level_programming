#!/usr/bin/python3
""" Task 9: Student to JSON """


class Student:
    """ Class that defines a student by
    attributes:
        first_name
        last_name
        age
    """

    def __init__(self, first_name, last_name, age):
        """ Function that instantiate attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        that retrieves a dictionary representation of a
        Student instance (same as 8-class_to_json.py)
        """

        return(self.__dict__)
