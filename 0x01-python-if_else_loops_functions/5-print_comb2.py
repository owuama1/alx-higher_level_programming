#!/usr/bin/python3

for i in range(100):
    # Print each number with a comma and space, except for the last one
    print("{:02d}".format(i), end=", " if i < 99 else "\n")
