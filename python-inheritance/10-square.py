#!/usr/bin/python3
"""
This module defines a class BaseGeometry
"""

# Importation of Rectangle class
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """ creation of a class which inherits from Rectangle class"""

    def __init__(self, size):
        """
        A class that defines a rectangle by its height and width

        Note:
        Square inherits from Rectangle
        size is a private attribute

        Args:
        size (int): the size of the square
        """

        # Rectangle.__init__ will validate 'size' for width and height
        # using BaseGeometry.integer_validator
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Note: is a public instance method
        """

        return self.__size * self.__size

    def __str__(self):
        """
        Returns the string representation of the Square object.
        """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
