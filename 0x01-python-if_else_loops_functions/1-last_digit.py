#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    var = number % 10
elif number < 0:
    var = (-number) % 10
    var *= -1
else:
    var = 0
print("Last digit of {:d} is {:d} ".format(number, var), end="")
if var > 5:
    print("and is greater than 5")
elif var == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
