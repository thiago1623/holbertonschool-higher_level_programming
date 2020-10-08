#!/usr/bin/python3
""" function that reads n lines of a text file """


def read_lines(filename="", nb_lines=0):
    """ function that reads n lines of a text file """
    with open(filename, encoding='utf8') as file:
        if nb_lines <= 0:
            for line in file:
                print(line, end="")
        else:
            for line in range(nb_lines):
                print(file.readline(), end="")
