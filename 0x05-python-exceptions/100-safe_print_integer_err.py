#!/usr/bin/python3
"""
function that prints an integer with "{:d}".format()
"""
from sys import stderr


def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
        else:
            print("{:d}.".format(value))
    except (ValueError, TypeError) as te:
        stderr.write('Exception: {}\n'.format(te))
        return (False)
    else:
        return (True)
