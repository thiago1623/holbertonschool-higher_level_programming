#!/usr/bin/python3
def print_last_digit(number):
    last = number % 10
    negative = (number % -10) * -1
    if number >= 0:
        print("{}".format(last), end='')
        return(last)
    else:
        print("{}".format(negative), end="")
        return(negative)
