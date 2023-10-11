#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        biggest_int = float('-inf')
        j = None

        for key, value in a_dictionary.items():
            if value > biggest_int:
                biggest_int = value
                j = key

        return (j)
    return (None)
