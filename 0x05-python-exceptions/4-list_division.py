#!/usr/bin/python3
"""
function that divides element by element 2 lists.
"""


def list_division(my_list_1, my_list_2, list_length):
    lists = []
    count = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            count = 1
        except TypeError:
            print("wrong type")
            count = 1
        except IndexError:
            print("out of range")
            count = 1
        finally:
            if count:
                count = 0
                lists.append(0)
            else:
                lists.append(result)
    return lists
