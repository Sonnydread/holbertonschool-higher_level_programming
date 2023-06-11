#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        RP = a / b
    except (TypeError, ZeroDivisionError):
        RP = None
    finally:
        print("Inside result: {}".format(RP))
    return RP
