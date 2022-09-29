#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    compute the square of all integers of a matrix
    args: nested list
    Return: square of eacc integer in the array
    """
    if matrix is None:
        return None
    return list(map(lambda y: [x**2 for x in y], matrix))

if __name__ == '__main__':
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
