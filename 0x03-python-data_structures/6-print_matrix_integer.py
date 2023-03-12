#!/usr/bin/python3
__name__="__main__"

def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for c in r:
            print("{:d}".format(c),end = " " if c != r[-1] else "")
        print()
