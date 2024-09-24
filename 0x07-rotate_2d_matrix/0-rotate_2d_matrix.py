#!/usr/bin/python3
"""implements a function that rotates a 2D matrix 90 degrees clockwise.
"""

def rotate_2d_matrix(matrix):
    """
    rotates a 2D matrix in place 90 degrees clockwise.
    Args:
        matrix (list) - list of lists.
    Return:
        Nothing.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()

