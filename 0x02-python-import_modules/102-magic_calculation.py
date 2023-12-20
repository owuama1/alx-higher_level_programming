#!/usr/bin/python3
import importlib


def magic_calculation(a, b):
    magic_module = importlib.import_module('magic_calculation_102')
    add = magic_module.add
    sub = magic_module.sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
