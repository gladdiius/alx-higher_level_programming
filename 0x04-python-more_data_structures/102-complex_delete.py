#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key = []
    for k, v in a_dictionary.items():
        if (v == value):
            key.append(k)
    if key:
        for delete in key:
            del a_dictionary[delete]
    return a_dictionary
