#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    add or replace a new key value in dict
    """
    if a_dictionary[key] is None:
        return None
    a_dictionary[key] = value
    return a_dictionary
