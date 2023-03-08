#!/usr/bin/python3
def uppercase(str):  
        for i in str:
            asci = ord(i)
            if 122 >= asci >= 97:
                asci = asci - 32
            print("{}".format(chr(asci)),end="")
print()
