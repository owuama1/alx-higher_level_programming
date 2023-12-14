#!/usr/bin/python3
def uppercase(str):
    output_str = ""
    for char in str:
        output_str += chr(ord(char) - (32 * ('a' <= char <= 'z')))
    print("{}".format(output_str))
