#!/usr/bin/python3
"""
This module defines a method that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    A function that creates an Object from a “JSON file” """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
