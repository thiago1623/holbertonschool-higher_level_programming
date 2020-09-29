#!/usr/bin/python3

"""
This is the "Rectangle"  module.
"""


class Rectangle:
    """
    A Rectangle class with attributes width and height, and
    methods area and perimiter.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __str__(self):
        empty_string = ""
        for i in range(self.__height):
            try:
                for j in range(self.__width):
                    empty_string += str(self.print_symbol)
            except Exception:
                empty_string += type(self).print_symbol
            if i is not self.__height - 1:
                empty_string += "\n"
            return empty_string

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
        ajsdnakjsdnaksj
