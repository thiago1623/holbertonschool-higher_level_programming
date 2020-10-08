#!/usr/bin/python3
"""
function that writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file """
    with open(filename, 'w', encoding="utf-8") as fd:
        fd.write(json.dumps(my_obj))
