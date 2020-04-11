#!/usr/bin/python3


def find_peak(list_of_integers):
    """
    find the peak element in a list
    """
    arr = list_of_integers
    if arr:
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return arr[i]
        return max(arr[0], arr[-1])
    return None
