#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value is int() is True:
            print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
