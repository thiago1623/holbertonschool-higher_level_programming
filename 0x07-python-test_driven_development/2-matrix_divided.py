#!/usr/bin/python3
"""
function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """ method that divides all elements of a matrix"""
    try:
        if not isinstance(div, (float, int)) or isinstance(div, bool):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        if not all(len(lts) == len(matrix[0]) for lts in matrix):
            raise TypeError("Each row of the matrix must have the same size")

        if not isinstance(matrix, list) or \
                len(matrix) == 0 or len(matrix[0]) == 0:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        for lts in matrix:
            if not isinstance(lts, list) or not len(lts) > 0 or not \
                 all(isinstance(column, (int, float)) for column in lts):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
        new_mtrx = []
        for i in matrix:
            new_mtrx.append(list(map(lambda new_num:
                            round(new_num / div, 2), i)))
        return new_mtrx
    except:
        raise
