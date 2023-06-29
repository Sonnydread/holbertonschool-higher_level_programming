#!/usr/bin/python3
"""Write a rectangle class"""


from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for yt in range(self.__y):
            print()
        for ht in range(self.__height):
            for xt in range(self.__x):
                print(" ", end="")
        for wt in range(self.__width):
            print("#", end="")
        print()

    def __str__(self):
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        txt = ("[Rectangle] ({}) {}/{} - {}/{}".format(i, x, y, w, h))
        return txt

    def update(self, *args, **kwargs):
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
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
