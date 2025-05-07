#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print("{} argument:".format((len(sys.argv) - 1)))
        i = 1
        for arg in sys.argv[1:]:
            print("{}: {}".format(i, arg))
    elif len(sys.argv) == 1:
        print("{} arguments.".format((len(sys.argv) - 1)))
    else:
        print("{} arguments:".format((len(sys.argv) - 1)))
        i = 1
        for arg in sys.argv[1:]:
            print("{}: {}".format(i, arg))
            i = i + 1
