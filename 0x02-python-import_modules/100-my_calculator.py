#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    numArgv = len(argv)

    if numArgv != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operators = argv[2]

    def notFoundOperator():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    def my_add():
        auxAdd = add(a, b)
        print("{:d} + {:d} = {:d}".format(a, b, auxAdd))
        return auxAdd

    def my_sub():
        auxSub = sub(a, b)
        print("{:d} - {:d} = {:d}".format(a, b, auxSub))
        return auxSub

    def my_mul():
        auxMul = mul(a, b)
        print("{:d} * {:d} = {:d}".format(a, b, auxMul))
        return auxMul

    def my_div():
        auxDiv = div(a, b)
        print("{:d} / {:d} = {:d}".format(a, b, auxDiv))
        return auxDiv

    optionsOperators = {
        "+": my_add,
        "-": my_sub,
        "*": my_mul,
        "/": my_div
    }
    optionsOperators.get(operators, notFoundOperator)()
