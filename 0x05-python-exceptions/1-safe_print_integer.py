"""
function that prints an integer with "{:d}".format()
"""


def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
        else:
            print("{:d}.".format(value))
    except:
        return False
    else:
        return True
