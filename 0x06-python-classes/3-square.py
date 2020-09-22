#!/usr/bin/python3
"""
class Square that defines a square by: (based on 2-square.py)
"""


class Square():
    """constructor"""

    def __init__(self, size=0):
        """instance attribute"""
        try:
            if isinstance(size, int) and size >= 0:
                self.__size = size
            elif not isinstance(size, int):
                raise TypeError()
            elif size < 0:
                raise ValueError()
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    def area(self):
        """Public instance method that return the square area"""
        return self.__size * self.__size
