#!/usr/bin/python3
"""
 class Square that defines a square by: (based on 4-square.py)
"""


class Square():
    """constructor"""

    def __init__(self, size=0):
        """instance attribute """
        self.__size = size

    @property
    def size(self):
        """method to retrieve it"""
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ return square area"""
        return self.__size ** 2
