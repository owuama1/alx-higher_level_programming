#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(uppercase_char), end='')
        else:
            # Print non-letter characters as they are
            print("{}".format(char), end='')

    # Print a newline at the end
    print()
