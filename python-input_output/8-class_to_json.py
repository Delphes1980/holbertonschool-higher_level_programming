#!/usr/bin/python3
"""
This module defines a method that writes a function that returns the dictionary
description with simple data structure (list, dictionary, string, integer and
boolean) for JSON serialization of an object
"""


def class_to_json(obj):
    """
    A function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object
    """
    return obj.__dict__
