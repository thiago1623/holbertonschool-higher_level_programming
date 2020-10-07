#!/usr/bin/python3
"""
class Square that inherits from Rectangle (9-rectangle.py):
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """docstring for ."""

    def __init__(self, size):
        """constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
