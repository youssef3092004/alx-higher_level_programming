#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for x in my_string:
        if x != "c" and x != "C":
            result += x

    print(result)
