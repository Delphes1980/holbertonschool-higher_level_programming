#!/usr/bin/python3
"""
This module defines a method that serialize and deserialize an objet
using pickle
"""

import pickle


class CustomObject:
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
        print("name: {}".format(self.name))
        print("age: {}".format(self.age))
        print("Is student: {}".format(self.is_student))

    def serialize(self, filename):
        """
    A function that serialize a Python dictionary to a JSON file """
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        A function that serialize a Python dictionary to a JSON file """
        if not filename:
            return None
        with open(filename, 'rb') as f:
            cls = pickle.load(f)
            return pickle.loads(f)
