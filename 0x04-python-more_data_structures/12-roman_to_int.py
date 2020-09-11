#!/usr/bin/python3


def roman_to_int(roman_string):
    if (roman_string is None) or (type(roman_string) != str):
        return 0

    add = 0
    rom_nums = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
    }

    length = len(roman_string)
    for i in range(0, length):
        if i == length - 1:
            add += rom_nums[roman_string[i]]
        elif rom_nums[roman_string[i]] >= rom_nums[roman_string[i + 1]]:
            add += rom_nums[roman_string[i]]
        else:
            add -= rom_nums[roman_string[i]]
    return add
