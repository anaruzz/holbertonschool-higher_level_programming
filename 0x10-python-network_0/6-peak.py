#!/usr/bin/python3


def find_peak(list_of_integers):
    """
    find the peak element in a list
    """

    if list_of_integers == []:
        return None
    arr = list_of_integers
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            return arr[i]
    return max(arr[0], arr[-1])
