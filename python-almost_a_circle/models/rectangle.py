#!/usr/bin/python3
"""Write a rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Write a rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """args: width, height, id"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """This is width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """This is height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This is height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X attributte"""
        return self.__x

    @x.setter
    def x(self, value):
        """X attributte"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y attributte"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y attributte"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """def area"""
        return self.__width * self.__height

    def display(self):
        """public method for print stdout charact # """
        print('\n' * self.__y, end="")
        for W in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """elements to work with"""
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        txt = ("[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h))
        return txt

    def update(self, *args, **kwargs):
        """We define arguments"""
        if len(args) != 0:
            if len(args) == 1:
                self.id = args[1]
            elif len(args) == 2:
                self.__width = args[1]
            elif len(args) == 3:
                self.__height = args[2]
            elif len(args) == 4:
                self.__x = args[3]
            elif len(args) == 5:
                self.__y = args[4]

        else:
            for key, value in kwargs.items():
                if key == "height":
                    self.__height = value
                elif key == "width":
                    self.__width = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value
                elif key == "id":
                    self.id = value

    def to_dictionary(self):
        """We have our dictionary"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
