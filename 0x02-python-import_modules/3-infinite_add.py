#!/usr/bin/python3
import sys
arg = sys.argv 
len = len(arg) -1 
sum = 0
for i in range(1,len+1):
        sum += int(arg[i])
        print("{}".format(sum))
