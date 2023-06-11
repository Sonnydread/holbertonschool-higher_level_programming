#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    kont = 0
    try:
        for item in my_list:
            if isinstance(item, int):
                print("{:d}".format(item), end="")
                kont += 1
                if kont == x:
                    break
    except TypeError:
        return kont
    print()
    return kont
