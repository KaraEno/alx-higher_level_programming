#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    replace an elment from a list at index idx with elem
    Args:
        my_list - list to search
        idx - the position to access
        elem - new elem to swap with
    Return:
        modified my_list
    """
    temp = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in range(len(my_list)):
        if i == idx:
            temp.insert(idx, element)
        else:
            temp.append(my_list[i])

