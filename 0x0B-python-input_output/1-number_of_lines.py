#!/usr/bin/python3
"""
function that returns the number of lines of a text file:
"""


def number_of_lines(filename=""):
    """ return the number of lines of text file"""
    count = 0
    with open(filename, encoding="utf-8") as fd:
        for lines in fd:
            count += 1
        return count
