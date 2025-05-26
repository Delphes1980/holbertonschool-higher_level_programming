#!/usr/bin/python3
"""
This module defines a class BaseGeometry
"""


class BaseGeometry:
    """ creation of an empty class"""

    def area(self):
        """
        Raise an exception for a non implemented class
        """
        raise Exception("area() is not implemented")
        pass
