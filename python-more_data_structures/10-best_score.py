#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest_key = None
    biggest = -1
    for key, value in a_dictionary.items():
        if value > biggest:
            biggest = value
            biggest_key = key
    return biggest_key
