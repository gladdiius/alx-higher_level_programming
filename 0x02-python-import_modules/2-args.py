#!/bin/python3
__name__="main__"
import sys
arg = sys.argv
len=len(arg)
x = 0
if len == 0:
        print("{} arguments.".format(arg))
elif len == 1:
        print("{}: argument.".format(arg))
        print("{} .".format(arg[0]))
else:
        print("{}: arguments.".format(arg))
        for i in arg:
            print("{}: {}".format(x+1, i))
