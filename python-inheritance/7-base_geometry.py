#!/usr/bin/python3
"""
This module defines a class BaseGeometry
"""


class BaseGeometry:
    """ creation of an empty class"""

    def area(self):
        """
        Raise an exception for a non implemented class

        Note: is a public instance method
        """
        raise Exception("area() is not implemented")
        pass

    def integer_validator(self, name, value):
        """
        Note:
        is a public instance method
        name is always a string

        Raises:
        TypeError: if value is not an integer
        ValueError: if value is <= 0
        """

        # Checks if value is strictly an integer and not a boolean
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        # Checks if value i <= 0
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        pass
