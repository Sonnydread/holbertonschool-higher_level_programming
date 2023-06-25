#!/usr/bin/python3
"""funct that returns a list of integers repre the Pascal triangle"""


def pascal_triangle(n):

    if n <= 0:
        return []

    pas = [[1]]
    for Y in range(n - 1):
        DUB = [1]
        for x in range(len(pas) - 1):
            DUB.append(pas[Y][x] + pas[Y][x + 1])
        DUB.append(1)
        pas.append(DUB)
    return pas
