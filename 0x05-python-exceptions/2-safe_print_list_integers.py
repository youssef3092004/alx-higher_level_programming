#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i, j = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            c += 1
        except (TypeError, ValueError):
            continue
        i += 1
    print()
    return c
