#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    DV = []
    try:
        for W in range(list_length):
            try:
                result = my_list_1[W] / my_list_2[W]
            except TypeError:
                print("wrong type")
                result = 0
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            except IndexError:
                print("out of range")
                result = 0
            DV.append(result)
    finally:
        while len(DV) < list_length:
            DV.append(0)
    return DV
