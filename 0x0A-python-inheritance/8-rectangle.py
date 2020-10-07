#!/usr/bin/python3
""" class Rectangle """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ constructor """
    def __init__(self, width, height):
        """instance method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
