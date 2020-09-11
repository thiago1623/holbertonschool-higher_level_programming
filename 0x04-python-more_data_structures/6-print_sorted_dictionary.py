#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    for r_keys in sorted(a_dictionary.keys()):
        print("{}: {}".format(r_keys, a_dictionary[r_keys]))
