#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            new_string.append(i)
    return "".join(new_string)
# join() function is used to reconstruct a string without
#  any separator between characters
