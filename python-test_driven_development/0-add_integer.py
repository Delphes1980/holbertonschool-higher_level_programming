#!/usr/bin/python3
"""
    Module description: a module that contains a function called add_integer
that add two integers

    Functions: add_integer(a, b=98):
    add two integers
"""


def add_integer(a, b=98):

    """
    Description: Add two integers
    a and b must be first casted to integers if they are float

    Parameters:
    a: first integer
    b: second integer with default value 98

    Returns: the sum of a and b

    Raises: TypeError if inputs are not integer or float
    """

    # Check if a is an integer or a float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if b is an integer or a float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # a and b casted to an integer if they're float
    a = int(a)
    b = int(b)
    result = a + b
    return result
