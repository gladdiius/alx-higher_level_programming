#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for i in range(2):
        if not len(tuple_a):
            tuple_a += (0, 0)
        elif len(tuple_a) < 2:
            tuple_a += (0, )

        if not len(tuple_b):
            tuple_b += (0, 0)
        elif len(tuple_b) < 2:
            tuple_b += (0, )

    return tuple((tuple_a[x] + tuple_b[x] for x in range(2)))
