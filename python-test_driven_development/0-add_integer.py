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
    Parameters:
    a: first integer
    b: second integer
    Returns: the sum of a and b
    Exceptions: TypeError
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    result = a + b
    return result
