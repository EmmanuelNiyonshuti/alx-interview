#!/usr/bin/python3
"""
coin change problem solution with greedy approach.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins
    needed to meet a given amount.

    Args:
        coins (list): A list of coin denominations.
        total (int): The total amount of money to make.

    Returns:
        int: The minimum number of coins needed to make the total,
             or -1 if it's not possible.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
        if total == 0:
            return count
    return -1
