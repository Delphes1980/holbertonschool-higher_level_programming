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

        # This call will use the inherited integer_validator method
        # (via BaseGeometry) and raise the error with “size” if
        # validation fails.
        BaseGeometry.integer_validator(self, "size", size)
        # Once ‘size’ has been validated, call the constructor of the parent
        # class (Rectangle) It will receive an already validated ‘size’, and
        # its own validation will pose no problem.
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
