#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    b = 0
    for i in range(len(my_list)):
        my_list[b] = my_list[a - 1]
        b += 1
        a -= 1
        return my_list
    for j in range(len(my_list)):
        print("{:d}".format(my_list[j]))

