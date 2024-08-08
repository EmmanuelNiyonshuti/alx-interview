#!/usr/bin/python3
"""
Module to generate a Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates a Pascal's triangle with 'n' rows.
    Args:
        n (int): The number of rows in the triangle.
    Returns:
        list of list of int: A list of lists where
        each inner list represents a row in a pascal's triangle.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i+1])
        new_row.append(1)
        triangle.append(new_row)
    return triangle
