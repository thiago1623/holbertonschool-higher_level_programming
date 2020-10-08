#!/usr/bin/python3
"""function that creates an Object from a “JSON file”: """
import json


def load_from_json_file(filename):
    """creates an Object"""
    with open(filename, encoding="utf-8") as fd:
        return json.load(fd)
