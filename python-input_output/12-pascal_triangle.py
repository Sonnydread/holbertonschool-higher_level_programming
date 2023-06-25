#!/usr/bin/python3
"""returns list of integers to be Pascal Triangle"""


def pascal_triangle(n):

    triangle = []
    for X in range(n):
        DUB = []
        for Z in range(X + 1):
            if Z == 0 or Z == X:
                DUB.append(1)
            else:
                DUB.append(triangle[X - 1][Z - 1] + triangle[X - 1][Z])
        triangle.append(DUB)
    return triangle
