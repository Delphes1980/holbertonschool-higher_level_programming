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
            raise ValueError("width must be >= 0")

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

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Note:
        area is a public instance method

        Returns:
        int: the area (width * height)
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Note:
        perimeter is a public instance method

        Returns:
        int: the perimeter (width + height) * 2
        """

        if self.__width == 0 or self.__height == 0:
            result = 0
            return result
        else:
            result = (self.__width + self.__height) * 2
            return result

    def __str__(self):
        """
        Returns the string representation of the rectangle
        for printing with '#' characters.

        Note:
        __str__ is a special method used by print() and str().

        Returns:
        str: a visual representation of the rectangle using '#' characters.
        Returns an empty string if width or height is 0.
        """

        # Checks if width or height are equal to 0
        if self.width == 0 or self.height == 0:
            return ""
        # Build the rectangle line by line:
        # ('#' * self.width + '\n') * (self.height - 1): creates all lines
        # except the last one, each ending with a newline.
        # The final + '#'*self.width: adds the last line without a newline
        # to avoid an extra empty line at the end.
        return ('#' * self.width + '\n') * (self.height - 1) + '#' * self.width

    def __repr__(self):
        """
        Returns the official string representation of the rectangle.

        Note:
        __repr__ is a special method used for debugging and developer use.

        Returns:
        str: a string that can recreate the object using eval(), in the format:
            ClassName(width, height)
        """

        # Returns "class_name object(width, height" in the output
        return (f"{self.__class__.__name__}{self.width, self.height}")
