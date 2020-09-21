#!/usr/bin/python3
"""
function that prints the first x elements of a list and only integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0

        for i in range(x):
            if isinstance(my_list[i], int):
                count += 1
                print("{:d}".format(my_list[i]), end="")
    except TypeError as e:
        print(e)
    else:
        print("")
        return count
