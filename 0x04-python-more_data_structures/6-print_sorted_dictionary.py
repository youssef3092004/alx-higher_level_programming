#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    x = list(a_dictionary.keys())
    x.sort()
    for y in x:
        print("{}: {}".format(y, a_dictionary[y]))
