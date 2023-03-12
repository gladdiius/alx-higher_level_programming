#!/usr/bin/python3
__name__="__main__"
def no_c(my_string):
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))

