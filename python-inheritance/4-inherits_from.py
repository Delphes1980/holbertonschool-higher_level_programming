#!/usr/bin/python3
"""
This module defines a method that returns True if the object is an instance of
a class that inherited (directly or indirectly) from the specified class
otherwise False
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of
    a class that inherited (directly or indirectly) from the specified class
    otherwise False
    """

    # Check if obj is an instance of the specific class, return False
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True  # It is a subclass instance
    return False  # Either it's a direct instance or unrelated
