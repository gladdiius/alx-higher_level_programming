#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    str1 = ''
    try:
        for i in range(x):
            str1 += str(my_list[i])
        print(str1)
    except IndexError:
        print(str1)
    x = 0
    for i in str1:
        x += 1
    return x
