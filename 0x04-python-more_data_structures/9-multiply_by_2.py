#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    tmp_dic = a_dictionary.copy()
    for i in tmp_dic.keys():
        tmp_dic[i] *= 2
    return tmp_dic
