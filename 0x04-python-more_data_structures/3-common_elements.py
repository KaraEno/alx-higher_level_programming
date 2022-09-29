#!/usr/bin/python3

def common_elements(set_1, set_2):
    b = set_1.intersection(set_2)
    return b

if __name__ == '__main__':
    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby" }
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))
