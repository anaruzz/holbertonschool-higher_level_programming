#!/usr/bin/python3
"""
Module that divides a matrix with an integers
matrix : list of lists of elements of type int or float
div: integer to divide matrix by
"""
def matrix_divided(matrix, div):
    """
    Returns new matrix
    """
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for i in matrix:
        if type(i) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    size_row = len(matrix[0])
    for i in matrix:
        if size_row != len(i):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not matrix:
        return matrix
    new_matrix = []
    for i in matrix:
        row = []
        for j in i:
            row.append(round((j / div), 2))
        new_matrix.append(row)
    return new_matrix
