#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_items = sorted(a_dictionary.items())
    for key, value in ordered_items:
        print("{}: {}".format(key, value))
