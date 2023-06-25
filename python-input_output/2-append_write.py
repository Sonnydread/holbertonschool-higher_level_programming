#!/usr/bin/python3
"""function that appends a string at the end of a text"""


def append_write(filename="", text=""):
    """func appends string at the end"""
    with open(filename, 'a') as myfile:
        return myfile.write(text)
