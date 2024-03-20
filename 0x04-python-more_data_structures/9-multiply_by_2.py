#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    array = {}
    for key, value in a_dictionary.items():
        array[key] = value * 2
    return array
