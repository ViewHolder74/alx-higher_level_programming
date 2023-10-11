#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix1 = []
    for row in matrix:
        new_row = [x ** 2 for x in row]
        matrix1.append(new_row)
    return (matrix1)
