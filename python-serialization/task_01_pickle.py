#!/usr/bin/python3
"""
This module defines a method that serialize and deserialize an objet
using pickle
"""

import pickle


class CustomObject:
    """ A custom class with name, age and is_student attributes
    and methods for display, serialization and deserialization """
    def __init__(self, name, age, is_student):
        """
        Initiates a custom instance of an object

        Args:
        name (string): the name of the object
        age (integer): the age of the object
        is_student (boolean): if the object is student or not
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        A function that prints out the object’s attributes """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance of the object to a file using pickle
        Returns None if an exception occurs during serialization"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from a file using pickle
        Returns the deserialized object, or None if the file is non-existent
        or malformed"""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            # Checks if the loaded object is of the expected type
            if isinstance(obj, cls):
                return obj
            else:
                # If the loaded objet is not of the expected type
                # it's malformed
                return None
        except Exception:
            return None
