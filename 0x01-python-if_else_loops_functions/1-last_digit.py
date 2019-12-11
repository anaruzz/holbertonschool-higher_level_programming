#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
var = number % 10
if var > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, var))
elif var == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, var))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, var))
