#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Use the symmetric difference method to find elems present in only one set
    diff_set = set_1.symmetric_difference(set_2)

    return diff_set
