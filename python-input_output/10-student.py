#!/usr/bin/python3
"""a class Student that defines a student by name, lname n age"""


class Student:
    """Clasify by name, last name n age"""
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        try:
            new = dict(filter(lambda e: e[0] in attrs, self.__dict__.items()))
            return new
        except Exception:
            return self.__dict__
