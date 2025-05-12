#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    biggest = my_list[0]
    for num in my_list:
        if num > biggest:
            biggest = num
        else:
            continue
    return biggest
