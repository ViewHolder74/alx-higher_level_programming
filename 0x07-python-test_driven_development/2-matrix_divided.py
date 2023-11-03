#!/usr/bin/python3
"""1. Divide a matrix"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    Raise TypeError and ZeroDiviionError with messages
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    excep_msg1 = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(excep_msg1)

    count = 0
    excep_msg2 = "Each row of the matrix must have the same size"

    for values in matrix:
        if not values or not isinstance(values, list):
            raise TypeError(excep_msg1)

        if count != 0 and len(values) != count:
            raise TypeError(excep_msg2)

        for num in values:
            if not type(num) in (int, float):
                raise TypeError(excep_msg2)

        count = len(values)

    result = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (result)
