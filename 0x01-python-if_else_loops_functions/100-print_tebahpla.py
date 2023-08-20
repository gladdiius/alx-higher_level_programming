#!/usr/bin/python3
for i in range(26):
    print('{}'.format(chr(122 - i)) if i % 2 == 0
          else '{}'.format(chr(90 - i)), end="")
