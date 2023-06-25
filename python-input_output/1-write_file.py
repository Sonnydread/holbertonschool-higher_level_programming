#!/usr/bin/python3
"""function writes a string to a text file"""


def write_file(filename="", text=""):
    """function writes a string to a text file"""
    with open(filename, 'w') as myfile:
        return myfile.write(text)
