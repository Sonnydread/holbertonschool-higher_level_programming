#!/usr/bin/python3
"""MyList inherits list"""


class MyList(list):
    """MyList inherits list"""

    def print_sorted(self):
        """print list, ascendenting"""

        print(sorted(self))
