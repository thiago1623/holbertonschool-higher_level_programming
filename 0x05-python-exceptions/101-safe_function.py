#!/usr/bin/python3
"""
function that executes a function safely.
"""
from sys import stderr


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return (res)
    except Exception as err:
        stderr.write('Exception: {}\n'.format(err))
        return (None)
