#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """docstring for ."""

    def __init__(self, width, height):
        """constructor"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """the area method"""
        return self.__width * self.__height
    """ Return rectangle """
    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
