#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    # Create a list of keys to delete
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]

    # Delete keys from the original dictionary
    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
