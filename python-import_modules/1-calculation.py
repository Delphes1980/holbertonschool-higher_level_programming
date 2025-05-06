#!/usr/bin/python3
import calculator_1

if __name__ == "__main__":
    a = 10
    b = 5
    result1 = calculator_1.add(a, b)
    print("{} + {} = {}".format(a, b, result1))
    result2 = calculator_1.sub(a, b)
    print("{} + {} = {}".format(a, b, result2))
    result3 = calculator_1.mul(a, b)
    print("{} + {} = {}".format(a, b, result3))
    result4 = calculator_1.div(a, b)
    print("{} + {} = {}".format(a, b, result4))
