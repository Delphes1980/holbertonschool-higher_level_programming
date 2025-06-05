#!/usr/bin/python3
""" This module defines a Student """


class Student:
    """ A class Student
    Args:
    first_name: Student's first name
    last_name: Student's last name
    age: Student's age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initiates a new Student instance

        Args:
        first_name: Student's first name
        last_name: Student's last name
        age: Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        A function that retrieves a dictionary representation of
        a Student instance

        Args:
        attrs: a list of string representing the attributes to retrieve.
        If None, all attributes are retrieved
        """
        # Checks if attrs is None
        if attrs is None:
            return self.__dict__
        else:
            # Checks if attrs is a list
            if isinstance(attrs, list):
                # If the list is empty, return an empty dictionary
                if not attrs:
                    return {}

                my_dict = {}
                for i in attrs:
                    # Checks if the requested attribute exists in
                    # the intance's __dict__
                    if i in self.__dict__:
                        # Add the attribute & its value to my_dict
                        my_dict[i] = getattr(self, i)
                return my_dict

    def reload_from_json(self, json):
        """
        A function that replaces all attributes of the Student instance

        Args:
        json: A dictionary containing attribute names (keys) and their
        corresponding values to update the Student instance.
        This dictionary typically comes from deserialized JSON data.
        """
        for key in json:
            setattr(self, key, json[key])
