#!/usr/bin/python3
if __name__ == "__main__":
    import sys
argv = sys.argv
l = len(argv)

if l > 1:
    if l == 2:
        print("{:d} argument:".format(l - 1))
        print("{:d}: {:s}".format(1, argv[1]))
    else:
        print("{:d} arguments:".format(l - 1))
        for i in range(1, l):
            print("{:d}: {:s}".format(i, argv[i]))
else:
    print("{:d} arguments.".format(l - 1))
