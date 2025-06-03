#!/usr/bin/python3
"""
This module defines a method that returns the JSON representation of an
object (string)
"""
import json


def to_json_string(my_obj):
    """
    A function that returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
