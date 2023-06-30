#!/usr/bin/python3
"""Base of all other classes in this project"""


import json


class Base:
    """Base of all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        new = []
        if list_objs is not None:
            for ele in list_objs:
                new.append(ele.to_dictionary())
        with open("{}.json".format(cls.__name__), 'w') as fle:
            fle.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            clase = cls(1, 1)
        elif cls.__name__ == "Square":
            clase = cls(1)

        clase.update(**dictionary)
        return clase

    @classmethod
    def load_from_file(cls):
        from os import path
        fl = "{}.json".format(cls.__name__)
        if not path.isfile(fl):
            return []
        with open(fl, 'r', encoding="utf-8") as fle:
            ls = cls.from_json_string(fle.read())
            for index in range(len(ls)):
                ls[index] = cls.create(**ls[index])
            return ls
