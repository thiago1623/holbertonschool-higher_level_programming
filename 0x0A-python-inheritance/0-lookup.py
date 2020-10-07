#!/usr/bin/python3
"""
function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """return the list of available"""
    return dir(obj)
