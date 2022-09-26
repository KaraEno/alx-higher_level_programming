#!/usr/bin/python3

def no_c(my_string):
    """
    Returns a copy of my_str without c or C
    Args:
        my_str - the string to filter
    """
    for i in my_string:
        if my_string[i] != 'c' or my_string[i] != 'C':
            print(my_string[i])
