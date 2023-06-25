#!/usr/bin/python3
"""function that reads my text file, then printed"""


def read_file(filename=""):
    """function that reads my text file, then printed"""
    with open(filename, 'r') as myfile:
        print(myfile.read(), end='')
