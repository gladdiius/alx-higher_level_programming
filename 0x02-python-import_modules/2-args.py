#!/usr/bin/python3
__name__="__main__"
import sys
arg = sys.argv 
len = len(arg) 

if len == 1:
    print("{} arguments.".format(len-1))
elif len == 2:
    print("{} argument:".format(len-1))
    print("{}: {}".format(len-1,arg[1]))
else:
    int("{} arguments:".format(len-1))
    for i in range(1,len):
        print("{:d}: {}".format(i, arg[i]))
