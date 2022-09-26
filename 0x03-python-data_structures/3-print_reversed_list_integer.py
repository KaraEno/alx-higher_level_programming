#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints integers in a list in reverse
    Args:
        my_list - list of integers defauult []
    """
    a = -1
    for i in range(len(my_list)):
        print("{:d}".format(my_list[a]))
        a -= 1

