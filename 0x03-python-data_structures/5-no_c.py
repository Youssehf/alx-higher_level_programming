#!/usr/bin/python3


def no_c(my_string):
    """removes all characters c and C from a string."""
    strList = [x for x in my_string if x not in "cC"]
    return ("".join(strList))
