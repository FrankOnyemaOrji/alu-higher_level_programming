#!/usr/bin/python3


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err))
        return False
    return True
