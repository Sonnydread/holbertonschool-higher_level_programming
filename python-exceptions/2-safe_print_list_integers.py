#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    kont = 0
    for W in range(x):
        try:
            print("{:d}".format(my_list[W]), end="")
        except (TypeError, ValueError):
            pass
        else:
            kont += 1
    print()
    return kont
