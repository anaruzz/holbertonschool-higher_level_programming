#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    line = []
    for i in range(n):
        row = []
        line.append(row)
        for j in range(0, i + 1):
            if j == 0 or j is i:
                line[i].append(1)
            else:
                line[i].append(line[i - 1][j - 1] + line[i - 1][j])
    return line
