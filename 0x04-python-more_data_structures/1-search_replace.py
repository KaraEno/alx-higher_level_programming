#!/usr/bin/python3
def search_replace(my_list, search, replace):

    """
    search and replace an element in a list
    Args:
        my_list - The list to search
        search - element to replace
        replace - subtitute for search
    """
    b = []
    for i in my_list:
        if i == search:
            b.append(replace)
        else:
            b.append(i)
    return b

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)

    print(new_list)
    print(my_list)
