#!/usr/bin/python3
""" Task 12: Pascal's Triangle."""


def pascal_triangle(n):
    """ Function that returns a list of lists of integers representing
    the Pascal's triange of n
    """

    my_list = []
    if n <= 0:
        return []
    for i in range(n):
        row = []

        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row1 = my_list[i - 1]
                value1 = row1[j - 1]
                value2 = row1[j]
                row.append(value1 + value2)

        my_list.append(row)
    return (my_list)
