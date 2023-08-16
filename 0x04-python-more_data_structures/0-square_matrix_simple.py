#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = matrix[:]
    return [col**2 for row in new_list for col in row]
