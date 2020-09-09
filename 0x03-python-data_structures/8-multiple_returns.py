#!/usr/bin/python3


def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        first_chr = sentence[0]
        tmp_tup = length, first_chr
        return(tmp_tup)
    else:
        return(0, None)
