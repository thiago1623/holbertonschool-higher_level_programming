#!/usr/bin/python3


def search_replace(my_list, search, replace):
    return (list(map(lambda num: replace if num is search else num, my_list)))
