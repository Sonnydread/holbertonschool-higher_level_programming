#!/usr/bin/python3
"""empty class BaseGeometry"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """empty BaseGeometry class"""

    def __init__(self, size):
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        REK = '[Rectangle] {}/{}'
        return REK.format(self.__size, self.__size)
