#!/usr/bin/python3
"""Class Square inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Write a square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Write a square class"""
        return f"""[{self.__class__.__name__}] ({self.id}) \
{self.x}/{self.y} - {self.width}"""

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        else:
            for key, value in kwargs.items():
                if 'id' == key:
                    self.id = value
                elif 'size' == key:
                    self.width = value
                    self.height = value
                elif 'x' == key:
                    self.x = value
                elif 'y' == key:
                    self.y = value

    def to_dictionary(self):
        """We have our dictionary"""
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y
        }
