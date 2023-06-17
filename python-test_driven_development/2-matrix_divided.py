#!/usr/bin/python3
"""Write a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):

    ms1 = "matrix must be a matrix (list of lists) of integers/floats"
    ms2 = "Each row of the matrix must have the same size"
    if type(matrix) != list:
        raise TypeError(ms1)
    for W in range(len(matrix)):
        if type(matrix[W]) != list:
            raise TypeError(ms1)
        if W != len(matrix) - 1:
            if len(matrix[W]) != len(matrix[W + 1]):
                raise TypeError(ms2)
        for R in range(len(matrix[W])):
            if type(matrix[W][R]) not in [int, float]:
                raise TypeError(ms1)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    fin = matrix.copy()
    for S in range(len(matrix)):
        fin[S] = list(map(lambda W: round(W / div, 2), matrix[S]))
    return fin
