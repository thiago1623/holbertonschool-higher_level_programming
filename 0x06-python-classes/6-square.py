#!/usr/bin/python3
"""
class Square that defines a square by: (based on 5-square.py)
"""


class Square():
    """constructor"""

    def __init__(self, size=0, position=(0, 0)):
        """instance attribute"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """method to retrieve it """
        return self.__size

    @size.setter
    def size(self, value):
        """method to set it"""
        try:
            if not isinstance(value, int):
                raise TypeError()
            if value < 0:
                raise ValueError()
            self.__size = value
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

    @property
    def position(self):
        """method to retrieve it"""
        return self.__position

    @position.setter
    def position(self, value):
        """method to set it"""
        try:
            if type(value) != tuple or len(value) != 2:
                raise TypeError()
            elif not all(isinstance(value, int) for i in value):
                raise TypeError()
            elif not all(i >= 0 for i in value):
                raise TypeError()
            self.__position = value
        except TypeError:
            print("position must be a tuple of 2 positive integers")

    def area(self):
        """instance method that return square area"""
        return self.__size ** 2

    def my_print(self):
        """method that prints in stdout the square with the character #:"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
