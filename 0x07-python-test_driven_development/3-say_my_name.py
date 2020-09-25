#!/usr/bin/python3
"""
 function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """print the first_name and last_name """
    try:
        first_string = "My name is"
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")

        print("{} {} {}".format(first_string, first_name, last_name))
    except:
        raise
