#!/usr/bin/python3
"""returns list of integers to be Pascal Triangle"""


def pascal_triangle(n):

    triangle = []
    for X in range(n):
        row = []
        for Z in range(X + 1):
            if Z == 0 or Z == X:
                row.append(1)
            else:
                row.append(triangle[X - 1][Z - 1] + triangle[X - 1][Z])
        triangle.append(row)
    return triangle
