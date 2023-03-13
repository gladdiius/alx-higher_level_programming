#!/usr/bin/python3
__name__="__main__"


def divisible_by_2(my_list=[]):
    multiple =[]
    for i in my_list:
        if i % 2 == 0: 
            multiple.append(True) 
        else: 
            multiple.append(False)
    return multiple
