#!/usr/bin/python3
for i in range(9):
    for x in range(10):
        if x > i:
            print("{}{}".format(i,x),end="")
            if i != 8:
                print(",",end=" ")
print()
