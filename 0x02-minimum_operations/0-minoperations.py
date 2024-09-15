#!/usr/bin/python3
"""
comprises an algorithm to calculate
the minimum number of operations to get n 'H' chars given n.
"""


def minOperations(n):
    """
    Calculates the minimum number of operations
    to get n 'H' characters.
    Args:
        n (int) - The target number of 'H' characters.
    Returns:
        int: The minimum number of operations required, or 0 if impossible.

    """
    if n <= 1:
        return 0
    operations = 0
    factors = 2
    while n > 1:
        while n % factors == 0:
            operations += factors
            n //= factors
        factors += 1
    return operations
