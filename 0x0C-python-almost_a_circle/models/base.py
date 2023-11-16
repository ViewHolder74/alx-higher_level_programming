#!/usr/bin/python3
""" Task 2: Base Class."""

import json


class Base:
    """ First class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialise and instantiate attributes."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function that returns  the JSON string
        representation of list_dictionaries.
        """

        if list_dictionaries is None or len(list_dictionaries) == []:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Function that writes the JSON string
        representation of list_objs to a file
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")

            else:
                my_list = [j.to_dictionary() for j in list_objs]
                f.write(Base.to_json_string(my_list))
