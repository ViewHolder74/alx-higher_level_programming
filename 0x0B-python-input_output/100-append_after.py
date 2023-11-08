#!/usr/bin/python3
""" Task 13 Search and Update"""


def append_after(filename="", search_string="", new_string=""):
    """" function that inserts a line of text to a file,
    after each line containing a specific string
    """

    lines = ""
    with open(filename) as f:
        for line in f:
            lines += line

            if search_string in line:
                lines += new_string

    with open(filename, "w") as f:
        f.write(lines)
