#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Get the sorted list of keys
    sorted_keys = sorted(a_dictionary.keys())

    # Print the dictionary by ordered keys
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
