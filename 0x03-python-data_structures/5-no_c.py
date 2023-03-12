#!/usr/bin/python3
__name__="__main__"
def no_c(my_string):
    eli = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            eli += i
        return eli
