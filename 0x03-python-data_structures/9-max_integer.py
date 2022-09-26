#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    find the maximum value of a list
    Args:
        my_list - list to search
    Return:
        None - if list is empty
        maximum of list
    """
    if len(my_list) == 0:
        return None
    new = sorted(my_list, reverse=True)
    return new[0]
