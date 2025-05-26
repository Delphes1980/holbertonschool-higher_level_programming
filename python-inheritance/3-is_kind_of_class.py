#!/usr/bin/python3
"""
This module defines a method that returns True if the object is an instance of
or if the object is an instance of a class that inherited from, the specified
class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class,or if
    the object is an instance of a clacc that inherited from the specified
    class, False otherwise
    """
    return isinstance(obj, a_class)
