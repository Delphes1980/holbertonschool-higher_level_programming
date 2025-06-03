#!/usr/bin/python3
""" This module defines a Student """


class Student:
    """ A class Student """

    def __init__(self, first_name, last_name, age):
        """
        A function that create the Object 'Student'
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        A function that retrieves a dictionary representation of
        a Student instance
        """
        return self.__dict__
