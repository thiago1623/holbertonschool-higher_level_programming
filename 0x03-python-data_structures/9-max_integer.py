#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    save_count = my_list[0]
    for i in my_list:
        if i > save_count:
            save_count = i
    return save_count
