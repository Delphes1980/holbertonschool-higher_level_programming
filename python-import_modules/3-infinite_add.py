#!/usr/bin/python3
import sys

if __name__ == "__main__":
    my_sum = 0
    for args in sys.argv[1:]:
        my_sum += int(args)
    print("{}".format(my_sum))
