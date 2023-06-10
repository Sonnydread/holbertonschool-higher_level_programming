#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    Kont = 0
    try:
        for W in range(x):
            print(my_list[W], end="")
            Kont += 1
    except IndexError:
        pass
    print()
    return Kont
