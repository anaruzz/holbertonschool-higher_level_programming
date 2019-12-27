#!/usr/bin/python3
def best_score(a_dictionary):
    m = 0
    if (a_dictionary):
        for val in a_dictionary:
            if m <= a_dictionary[val]:
                m = a_dictionary[val]
                max = val
        return (max)
    else:
        return (None)
