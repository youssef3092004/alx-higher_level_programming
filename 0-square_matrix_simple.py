#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    array = []
    for List in matrix:
        row = list(map(lambda i: i ** 2, List))
        array.append(row)
    return (array)
