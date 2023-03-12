#!/usr/bin/python
__name__="__main__"


def new_in_list(my_list, idx, element):
    my_list2 = my_list
    list_len = len(my_list2)-1
    if idx < 0:
        return my_list
    elif idx > list_len:
        return my_list
    else:
        my_list2[idx] = element
        return my_list2
