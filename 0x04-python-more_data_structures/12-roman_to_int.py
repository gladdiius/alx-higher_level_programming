#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {
         'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000
         }
    x = 0
    len1 = len(roman_string) - 1
    flage = 0
    flage2 = 0
    for i in roman_string:
        if (len1 + 1) >= 2:
            if roman_string[-1] != 'I':
                roman['I'] = -1
            if roman_string[0] == 'X' and not flage:
                roman['X'] = -10
                flage = 1
            if roman_string[0] == 'C' and not flage2:
                roman['C'] = -100
                flage2 = 1
        x += roman[i]
        if flage:
            roman['X'] = 10
        if flage2:
            roman['C'] = 100
    return x
