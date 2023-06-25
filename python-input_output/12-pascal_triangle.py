#!/usr/bin/python3
"""returns list of integers to be Pascal Triangle"""


def pascal_triangle(n):

    triangle = []
    for i in range(n):
        DUB = []
        for Z in range(i + 1):
            if Z == 0 or Z == i:
                DUB.append(1)
            else:
                DUB.append(triangle[i - 1][Z - 1] + triangle[i - 1][Z])
        triangle.append(DUB)
    return triangle
