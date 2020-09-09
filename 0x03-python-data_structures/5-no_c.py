#!/usr/bin/python3


def no_c(my_string):
    cp_string = list(my_string)
    for i in cp_string:
        if i == 'C' or i == 'c':
            cp_string.remove(i)
    return "".join(cp_string)
