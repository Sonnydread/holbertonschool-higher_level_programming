#!/usr/bin/python3
"""square class"""


class Square:
    """attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """size class of da square
        Args:
            size (int): must be integer
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()

        else:
            for W in range(self.__position[1]):
                print()
            for M in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for Y in range(self.__size):
                    print("#", end="")
                print()
