#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i >= 'a' and i <= 'z':
            upper = chr(ord(i) - 32)
        else:
            upper = i
        print("{:s}".format(upper), end='')
    print()
# chr() function returns the character that represents the specified unicode
# it's the opposite of ord() function
