#!/usr/bin/python3
"""
class Square that defines a square by: (based on 1-square.py)
"""


class Square():
    """constructor"""

    def __init__(self, size=0):
        """instance attribute"""
        try:
            if size is not isinstance(size, int):
                raise TypeError()
            if size < 0:
                raise ValueError()
            if isinstance(size, int) and size >= 0:
                self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
