#!/usr/bin/python3
i = 97
while i <= 122:
    if i != 111 or i != 113:
        print("{:c}".format(i), end="")
        i += 1
