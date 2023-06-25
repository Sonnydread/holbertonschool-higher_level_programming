#!/usr/bin/python3
"""function that creates an object from a JSON file"""


import json


def load_from_json_file(filename):
    """function that creates an object from a JSON file"""
    with open(filename) as myfile:
        return json.load(myfile)
