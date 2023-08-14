#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            if element:
                print("{:d}".format(element), end=" ")
        if row != matrix[(len(matrix) -1)]:
            print()
