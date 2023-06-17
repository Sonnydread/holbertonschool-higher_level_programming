#!/usr/bin/python3
"""A function that adds 2 nums"""


def add_integer(a, b=98):
    """Result of a + b"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
