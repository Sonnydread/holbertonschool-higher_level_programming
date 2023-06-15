#!/usr/bin/python3
"""square class"""


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
        else:
            self.__size = size

    def area(self):
        """Calculate the area of a square

        Returns:
            int: The area of a square

        """
        return self.__size * self.__size
