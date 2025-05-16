#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_sign = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    num = 0
    if roman_string is None or type(roman_string) is not str:
        return 0
    for i in range(len(roman_string)):
        # retrieve the integer value associated with the current symbol
        current = roman_sign.get(roman_string[i])
        if i + 1 < len(roman_string):  # Check if there's another element
            # retrieve the integer value associated with the next symbol
            next = roman_sign[roman_string[i + 1]]
            if current < next:
                num = num - current
            else:
                num = num + current
        else:
            num = num + current
    return num
