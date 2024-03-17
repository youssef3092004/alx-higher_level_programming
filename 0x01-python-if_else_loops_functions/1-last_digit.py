#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
AS = number % 10
if number < 0:
    x = abs(number) % 10 * -1
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, x))
elif AS > 0:
    if AS > 5:
        print("Last digit of {:d} is {:d} and is greater than 5".format(number, AS))
    else:
        print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, AS))
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, 0))
