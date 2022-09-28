#!/usr/bin/python3
    
def square_matrix_simple(matrix=[]):
    return list(map(lambda y: [x**2 for x in y]), matrix)
