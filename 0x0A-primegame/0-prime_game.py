#!/usr/bin/python3
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
        nums (list) - list of integers.
    Return:
        str: "Ben" if Ben wins, "Mary" if Mary wins.
    """
    if not nums or x <= 0:
        return None
    max_num = max(nums)
    primes = sieve_erastosthenes(max_num)
    ben = 0
    maria = 0
    for n in nums:
        primes_count = 0
        for p in primes:
            if p <= n:
                primes_count += 1
        if primes_count == 0:
            ben += 1
        if primes_count % 2 == 0:
            ben += 1
        elif primes_count % 2 != 0:
            maria += 1
    if ben > maria:
        return "Ben"
    elif ben < maria:
        return "Maria"
    return None

