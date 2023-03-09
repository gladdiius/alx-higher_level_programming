#!/usr/bin/python3
import sys
__name__ = "__main__"
arg = sys.argv 
sum = 0
for i in arg:
    if i != arg[0]:
        sum += int(i)
print("{}".format(sum))
