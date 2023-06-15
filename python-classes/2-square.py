#!/usr/bin/python3
"""size of da square"""


class Square:
    """attribute"""
    def __init__(self, size=0):
        """size class of da square

    Args:
        size (int): must be integer
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
