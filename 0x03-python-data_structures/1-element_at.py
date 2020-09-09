#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < len(my_list) and idx >= 0:
        return my_list[idx]
    elif idx < 0 and idx > len(my_list):
        return None
