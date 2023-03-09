#!/usr/bin/python3
__name__="main__"
import sys
len = len(sys.argv)
x = 0
if len == 0:
    print("{} arguments.".format(len))
elif len == 1:
    print("{}: argument.".format(len))
    print("{} .".format(sys.argv[0]))
else:
    print("{}: arguments.".format(len))
    for i in sys.argv:
        print("{}: {}".format(x+1, i))
