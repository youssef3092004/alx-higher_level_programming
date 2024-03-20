#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
oj = "and is less than 6 and not 0"
jo = "and is greater than 5"
AS = number % 10
if number < 0:
    x = abs(number) % 10 * -1
    print("Last digit of {:d} is {:d} {:s}".format(number, x, oj))
elif AS > 0:
    if AS > 5:
        print("Last digit of {:d} is {:d} {:s}".format(number, AS, jo))
    else:
        print("Last digit of {:d} is {:d} {:s}".format(number, AS, oj))
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, 0))
