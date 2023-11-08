#!/usr/bin/python3
""" Task 13 Search and Update"""


def append_after(filename="", search_string="", new_string=""):
    """" function that inserts a line of text to a file,
    after each line containing a specific string
    """

    with open(filename) as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + "\n")
