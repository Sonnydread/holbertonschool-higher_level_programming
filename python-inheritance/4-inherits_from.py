#!/usr/bin/python3
"""Function that return True if is no False"""


def inherits_from(obj, a_class):
    """Return False or True"""

    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
