#!/usr/bin/python3
def uppercase(str):
    for i in range(str):
        if i >= '97' and i <= '122':
            print("{:s}".format(i - 32))
