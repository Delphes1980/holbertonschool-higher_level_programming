#!/usr/bin/python3
"""
    Module description: module that contains a function called say_my_name
that prints "My name is <first name> <last name>"

    Functions: say_my_name(first_name, last_name):
    prints first and last name given
"""


def say_my_name(first_name, last_name=""):
    """
    Description: Prints first and last name given
    first_name and last_name must be strings

    Parameters:
    first_name: first name given by user
    last_name: last name given by user

    Returns: prints first and last name given by user

    Raises:
    TypeError if inputs are not string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
