#!/usr/bin/python3
"""
 class Square that defines a square by: (based on 3-square.py)
"""


class Square():
    """constructor"""

    def __init__(self, size=0):
        """ instance attribute """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if isinstance(value, int):
                self.__size = value
            elif not isinstance(value, int):
                raise TypeError()
            elif value < 0:
                raise ValueError()
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    def area(self):
        """ return square area """
        return self.__size * self.__size
