#!/usr/bin/python3
"""
This module defines a method that returns a list of attributes
and methods of an object.
"""


class MyList(list):
    """  A class MyList that inherits from list"""

    def print_sorted(self):
        """
        prints the sorted list of all the attributes and methods of an object
        """
        print(sorted(self))
