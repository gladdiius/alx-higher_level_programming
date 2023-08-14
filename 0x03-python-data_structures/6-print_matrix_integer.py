#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            if element:
                print("{}".format(element), end=" ")
        if row != matrix[(len(matrix) -1)]:
            print()
