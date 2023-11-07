#!/usr/bin/python3
""" Task 5: Save Objects to a file """

import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file,
    using a JSON representation:
    """

    with open(filename, "w", encoding="utf-8") as f:
        """ Open Json File """
        json.dump(my_obj, f)
