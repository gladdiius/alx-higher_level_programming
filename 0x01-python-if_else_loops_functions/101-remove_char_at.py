#!/usr/bin/python3
def remove_char_at(str, n):
    new = ''
    position = 0
    for i in range(len(str)):
        if position != n:
            new += str[i]
            position += 1
    return new
