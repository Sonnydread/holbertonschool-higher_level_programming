#!/usr/bin/python3
"""square class"""


class Square:
    """attribute"""
    def __init__(self, size=0):
        """size class of da square
        Args:
            size (int): must be integer
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        for R in range(self.__size):
            for S in range(self.__size):
                print("#", end="")
            print()
