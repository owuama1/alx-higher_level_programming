#!/usr/bin/python3

def lookup(obj):
    attributes_and_methods = []

    for attribute in dir(obj):
        if not callable(getattr(obj, attribute)) or attribute.startswith('__'):
            attributes_and_methods.append(attribute)

    return attributes_and_methods
