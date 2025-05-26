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

        # Checks if value is an integer
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        # Checks if value i <= 0
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        pass


class Rectangle(BaseGeometry):
    """ creation of an empty class"""

    def __init__(self, width, height):
        """
        A class that defines a rectangle by its height and width

        Note:
        Rectangle inherits from BaseGeometry
        width and height are private attributes

        Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
