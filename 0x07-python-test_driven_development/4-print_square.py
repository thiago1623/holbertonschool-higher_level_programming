#!/usr/bin/python3
"""
function that prints a square with the character #.
"""


def print_square(size):
    """print square"""
    try:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        if isinstance(size, bool):
            raise TypeError("size must be an integer")

        for i in range(int(size)):
            print("#" * int(size))
    except:
        raise
