#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    return [replace if search/x == 1 else x for x in new_list]
