#!/usr/bin/env python3
"""
comprises prime game challenge implementation.
"""


def sieve_erastosthenes(n):
    """
    implements sieve erastosthenes algorithm.
    """
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = []
    for i in range(2, n + 1):
        if prime[i]:
            primes.append(i)
    return primes


def isWinner(x, nums):
    """
    determines the winner after x rounds of the prime game.
    args:
        x (int) - number of rounds.
        nums (list) - list of integers for each round.
    Returns:
        str: "Ben" if Ben wins, "Mary" if Mary wins.
    """
    if not nums or x <= 0:
        return None
    ben = 0
    mary = 0
    i = 0
    while i < x:
        for n in nums:
            primes = sieve_erastosthenes(n)
            primes_count = len(primes)
            if primes_count == 0:
                ben += 1
            if primes_count % 2 == 0:
                ben += 1
            elif primes_count % 2 != 0:
                mary += 1
        i += 1

    if ben > mary:
        return "Ben"
    elif mary < ben:
        return "Mary"
    else:
        return None
