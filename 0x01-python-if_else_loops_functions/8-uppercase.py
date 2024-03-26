#!/usr/bin/python3
def uppercase(str):
    final = ''
    for x in str:
        if ord('a') <= ord(x) >= ord('z'):
            final += chr(ord(x) - 32)
        else:
            final += x
        print("{:s}".format(final))
