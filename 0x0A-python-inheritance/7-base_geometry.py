#!/usr/bin/python3
"""  class BaseGeometry (based on 6-base_geometry.py). """


class BaseGeometry():
    """docstring forBaseGeometry."""
    def area(self):
        raise Exception("area() is not implemented")

    """ Public instance method:  """
    def integer_validator(self, name, value):
        try:
            if not isinstance(value, int) or isinstance(value, bool):
                raise TypeError("{} must be an integer".format(name))
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
        except:
            raise
