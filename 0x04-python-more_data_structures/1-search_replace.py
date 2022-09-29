#!/usr/bin/python3
def search_replace(my_list, search, replace):

    b = []
    for i in mylist:
        if i == search:
            b.append(replace)
        else:
            b.append(i)
    return b
