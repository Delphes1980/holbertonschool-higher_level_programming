#!/usr/bin/python3
exec("import calculator_1 as calc")

if __name__ == "__main__":
    a = 10
    b = 5
    result1 = calc.add(a, b)
    print("{} + {} = {}".format(a, b, result1))
    result2 = calc.sub(a, b)
    print("{} - {} = {}".format(a, b, result2))
    result3 = calc.mul(a, b)
    print("{} * {} = {}".format(a, b, result3))
    result4 = calc.div(a, b)
    print("{} / {} = {}".format(a, b, result4))
