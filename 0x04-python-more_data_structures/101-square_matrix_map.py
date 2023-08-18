#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = matrix[:]
    return list(map(lambda x :list(map(lambda y: (y**2), x)), new_list))
