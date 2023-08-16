#!/usr/bin/python3
def best_score(a_dictionary):
    max_keys = None
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value == max(a_dictionary.values()):
                max_keys = key
    return max_keys
