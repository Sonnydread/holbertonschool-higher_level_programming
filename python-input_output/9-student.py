#!/usr/bin/python3
"""class Student that defines a student by name, last name n age"""


class Student:
    """Clasify by name, last name n age"""
    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
