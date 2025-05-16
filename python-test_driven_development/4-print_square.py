#!/usr/bin/python3
"""
    Module description: module that contains a function called print_square
that prints a square with the character #

    Functions: print_square(size):
    prints q square with the character #
"""


def print_square(size):
    """
    Description: Prints a square with the character #
    size must be an integer
    size can't be less than 0, integer or float

    Parameters:
    size: the size length of the square

    Returns: prints the square with the character #

    Raises:
    TypeError if size is not an integer
    TypeError if size is a float AND less than 0
    ValueError if size is less than 0
    """

    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is a float AND less than 0
    if size is type(float):
        if size < 0:
            raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#", end='')
        for j in range(size):
            print("#", end='')
        print()
