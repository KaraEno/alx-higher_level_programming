#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    for key, value in a_dictionary.items():
        print("{:s} : {:d}".format(key, value * 2))
    return list(a_dictionary)
