#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)
