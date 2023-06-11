#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    DV = [0] * list_length
    for W in range(list_length):
        try:
            DV[W] = my_list_1[W] / my_list_2[W]
        except TypeError:
            print("wrong type")
            DV[W] = 0
        except ZeroDivisionError:
            print("division by 0")
            DV[W] = 0
        except IndexError:
            print("out of range")
            DV[W] = 0
    return DV
