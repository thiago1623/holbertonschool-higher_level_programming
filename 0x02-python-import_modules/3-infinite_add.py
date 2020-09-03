#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    try:
        res = sum([int(num) for num in argv[1:]])
        print("{}".format(res))
    except ValueError:
        print("Please enter a number")
