#!/usr/bin/python3
"""empty class BaseGeometry"""


class BaseGeometry:
    """empty BaseGeometry class"""

    def area(self):
        """instance method area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate da integer"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
