#!/usr/bin/python3
"""
This module defines a method that write a script that adds all arguments to
a Python list, and then save them to a file
"""
import json  # For JSON serialization/deserialization
import os  # For OS-related operations, like checking file existence
import sys  # For accessing command-line arguments


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = 'add_item.json'  # The target JSON file
my_list = []

# Check if the file exists and load its content if it does
if os.path.exists(filename):
    my_list = load_from_json_file(filename)

# Extend the list with new command-line arguments (excluding script name)
my_list.extend(sys.argv[1:])
# Save the updated list back to the JSON file
save_to_json_file(my_list, filename)
