#!/usr/bin/python3
def no_c(my_string):
    """removes all characters c and C from a string."""
    strList = list(my_string)
    strList = [x for x in strList if x != "c" and x != "C"]
    return"".join(strList)
