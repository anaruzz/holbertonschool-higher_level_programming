#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    l = len(argv)
    s = 0
    for i in range(1, l):
        s = int (s + argv[i])
    print("{:d}".format(s))
