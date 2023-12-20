#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    # Convert arguments to integers and sum them
    result = sum(int(arg) for arg in argv[1:])

    # Print the result
    print(result)
