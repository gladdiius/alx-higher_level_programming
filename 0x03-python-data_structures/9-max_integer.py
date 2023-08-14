#!/usr/bin/python3
def max_integer(my_list=[]):
    big = my_list[0]
    for i in my_list:
        if big < i:
            big = i
    return big
