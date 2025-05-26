#!/usr/bin/python3
"""
This module defines a class BaseGeometry
"""


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
