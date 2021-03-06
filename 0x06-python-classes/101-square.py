#!/usr/bin/python3
"""
class Square that defines a square by: (based on 6-square.py)
"""


class Square:
    """constructor"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """method to retrieve it"""
        return self.__size

    @size.setter
    def size(self, size):
        """method to set it"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """method to retrieve it"""
        return self.__position

    @position.setter
    def position(self, value):
        """method to set it"""
        if type(value) != tuple or len(value) != 2 or \
           not all([type(i) == int for i in value]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __repr__(self):
        """return the object representation"""
        return (self.get_str())

    def area(self):
        """return the square area"""
        return self.__size * self.__size

    def get_str(self):
        """method to set it"""
        total = ""
        if self.__size == 0:
            total += "\n"
            return total
        for i in range(self.__position[1]):
            total += "\n"
        for i in range(self.__size):
            total += (" " * self.__position[0])
            total += ("#" * self.__size)
            if i is not (self.__size - 1):
                total += "\n"
        return total

    def my_print(self):
        """method to set it"""
        print(self.get_str())
