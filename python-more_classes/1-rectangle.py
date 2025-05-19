#!/usr/bin/python3
"""
This module defines a class Rectangle that represents a rectangle shape.
"""


class Rectangle:
    """ A class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
        A class that defines a rectangle by its height and width

        Note:
        __init__ method assign values to object properties
        width is a private instance attribute
        height is a private instance attribute

        Attributes:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for the width attribute
        The getter property retrieves the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width attribute.
        Ensures that the value is an integer >= 0
        """

        # Checks is width is an integer
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        # Checks if width is positive
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ Getter for the height attribute
        The getter property retrieves the height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height attribute.
        Ensures that the value is an integer >= 0
        """

        # Checks if height is an integer
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        # Checks if height is positive
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
