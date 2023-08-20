#!/usr/bin/python3
char = 122
for i in range(26):
    print(chr(char) if i % 2 == 0 else chr(char-32), end="")
    char -= 1
