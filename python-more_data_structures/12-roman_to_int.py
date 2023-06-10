#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    roman = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    result = 0
    R = 0
    while R < len(roman_string):
        if (
            R + 1 < len(roman_string) and
            roman.get(roman_string[R]) < roman.get(roman_string[R + 1])
        ):
            result += (
                roman.get(roman_string[R + 1]) -
                roman.get(roman_string[R])
            )
            R += 2
        else:
            result += roman.get(roman_string[R])
            R += 1
    return result
