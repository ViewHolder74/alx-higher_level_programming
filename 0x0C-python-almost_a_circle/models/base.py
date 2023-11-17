#!/usr/bin/python3
""" Task 2: Base Class."""

import json
import csv
import turtle


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

    @staticmethod
    def from_json_string(json_string):
        """Function that return the list of the JSON string
        representation json_string.
        """

        if json_string is None or json_string == "[]":
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Function that returns an instance with all attributes
        already set
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                obj = cls(4, 6)

            else:
                obj = cls(4)

            obj.update(**dictionary)
            return (obj)

    @classmethod
    def load_from_file(cls):
        """Function that returns a list of instances."""

        filename = cls.__name__ + ".json"
        try:
            with open(filename) as f:
                my_list = Base.from_json_string(f.read())
                return ([cls.create(**j) for j in my_list])

        except IOError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Function that serializes CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")

            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Function that deserializes CSV"""

        filename = cls.__name__ + ".csv"

        try:
            with open(filename) as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]

                dicts = csv.DictReader(f, fieldnames=fieldnames)
                dicts = [
                    dict([k, int(v)] for k, v in d.items())
                    for d in dicts
                    ]
                return (
                    [cls.create(**d) for d in dicts]
                )

        except IOError:
            return ([])
