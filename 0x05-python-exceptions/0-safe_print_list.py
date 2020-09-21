#!/usr/bin/python3
"""
function that prints x elements of a list
"""


def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
    except IndexError:
        return i
    else:
        return x
    finally:
        print("")
