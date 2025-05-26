#!/usr/bin/python3
"""
This module defines a method that returns a list of attributes
and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Attributes:
    obj (list): the object to be listed
    """
    return dir(obj)
