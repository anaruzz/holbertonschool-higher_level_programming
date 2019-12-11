#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        var = number % 10
    elif number < 0:
        var = (-number) % 10
    else:
        var = 0
    print("{:d}".format(var), end="")
    return (var)
