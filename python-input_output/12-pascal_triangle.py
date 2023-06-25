#!/usr/bin/python3
"""funct that returns a list of integers repre the Pascal triangle"""


def pascal_triangle(n):
    """representing the Pascal's triangle of n"""
    if n <= 0:
        return []

    pas = [[1]]
    for i in range(n - 1):
        DUB = [1]
        for x in range(len(pas) - 1):
            DUB.append(pas[i][x] + pas[i][x + 1])
        DUB.append(1)
        pas.append(DUB)
    return pas
