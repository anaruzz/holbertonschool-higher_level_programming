#!/usr/bin/python3


def find_peak(list_of_integers):
    """
    find the peak element in a list
    """
    l = list_of_integers
    if l:
        if len(l) < 2:
            return l[0]
        if l[0] > l[1]:
            return l[0]
        if l[-1] > l[-2]:
            return l[-1]
        for i in range(1, len(l) - 1):
            if l[i] > l[i - 1] and l[i] > l[i + 1]:
                return l[i]
    return None
