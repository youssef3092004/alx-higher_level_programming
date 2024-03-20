#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    array = []
    for i in matrix:
        j = i(map(lambda i: i ** 2, i))
        array.append(j)
    return (array)
