#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    coppy = my_list[:]
    if 0 <= idx < len(my_list):
        coppy[idx] = element
        return(coppy)
    return(my_list)
