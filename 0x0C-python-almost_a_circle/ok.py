#!/usr/bin/python3
def same(l1, l2):
    l = []
    for i in l1:
        if i in l2:
            l.append(i)
    return l

l1 = [1, 2, 3, 4]
l2 = [2, 5, 3, 4]
print(same(l1, l2))
