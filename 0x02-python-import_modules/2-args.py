#!/usr/bin/python3
import sys
l= len(sys.argv)
if l > 1:
    if l == 2:
        print("{:d} argument:".format(l - 1))
        print("{:d}: {:s}".format(1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(l - 1))
        for i in range(1, l):
            print("{:d}: {:s}".format(i, sys.argv[i]))
else:
    print("{:d} arguments.".format(l - 1))
