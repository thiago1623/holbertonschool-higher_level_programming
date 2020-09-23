#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    Square = __import__('101-square').Square

    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
