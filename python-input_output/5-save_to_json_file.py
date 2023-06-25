#!/usr/bin/python3
"""function that writes an object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an object to a text file"""
    with open(filename, "w") as myfile:
        myfile.write(json.dumps(my_obj))
