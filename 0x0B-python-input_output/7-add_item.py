#!/usr/bin/python3
"""
Script Name: add_to_list_and_save.py
Description: This script adds all command-line arguments to a Python list and
             then saves them to a file named add_item.json using the
             save_to_json_file and load_from_json_file functions.
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    # Get existing list from file, or create empty list if file doesn't exist
    try:
        existing_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_list = []

    # Add command-line arguments to the list
    new_items = sys.argv[1:]
    existing_list.extend(new_items)

    # Save the updated list to the file
    save_to_json_file(existing_list, 'add_item.json')


if __name__ == "__main__":
    main()
