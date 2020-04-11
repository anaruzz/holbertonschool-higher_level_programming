#!/usr/bin/python3


def find_peak(list_of_integers):
    """
    find the peak element in a list
    """

    if list_of_integers == []:
        return None
    length = len(list_of_integers)
    for i in range(length):
        current = list_of_integers[i]
        n = list_of_integers[i+1]
        p = list_of_integers[i-1]
        if current >= n and current >= p:
            return current
