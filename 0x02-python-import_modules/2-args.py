#!/usr/bin/python3
__name__="__main__"
import sys
arg = sys.argv 
len = len(arg) -1 

if len == 0:
    print("{} arguments.".format(len))
elif len == 1:
    print("{} argument:".format(len))
    print("{}: {}".format(len,arg[1]))
else:
    print("{} arguments:".format(len))
    for i in range(1,len+1):
        print("{:d}: {}".format(i, arg[i]))
