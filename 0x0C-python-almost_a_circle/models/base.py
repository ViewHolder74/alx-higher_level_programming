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

    def to_json_string(list_dictionaries):
        """Function that returns  the JSON string
        representation of list_dictionaries.
        """

        if list_dictionaries is None:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))
