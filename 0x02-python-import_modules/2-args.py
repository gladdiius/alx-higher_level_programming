#!/usr/bin/python3
__name__="__main__"
import sys
arg = sys.argv #list
len = len(arg)
x = 0
if len == 0:
    print("{} arguments.".format(len))
elif len == 1:
    print("{}: argument.".format(len))
    print("{} .".format(arg[0]))
else:
    print("{}: arguments.".format(len))
    for i in arg:
        print("{}: {}".format(x+1, i))
