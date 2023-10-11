#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    chars = sorted(a_dictionary.keys())
    for i in chars:
        print("{}: {}".format(i, a_dictionary[i]))
