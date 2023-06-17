#!/usr/bin/python3
"""a function that prints a square"""


def print_square(size):
    if type(size) is [float] and size < 0:
        raise TypeError("size must be an integer")
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for W in range(size):
        for S in range(size):
            print("#", end="")
        print()
