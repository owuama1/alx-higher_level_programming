#!/usr/bin/python3

# Iterate over ASCII values for lowercase letters

for i in range(97, 123):
    if i != 101 and i != 113:
        print("{}".format(chr(i)), end='')
