#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a copied list at a specific position."""
    newCopy = my_list.copy()
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    newCopy[idx] = element
    return newCopy
