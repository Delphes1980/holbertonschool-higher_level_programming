#!/usr/bin/python3
for i in range(97, 123):
    if i == 101 or i == 113:  # Print alphabet except 'e' and 'q'
        continue
    print("{:c}".format(i), end='')
