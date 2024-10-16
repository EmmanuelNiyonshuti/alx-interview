# 0x0A-primegame

- This project implements a solution for the Prime Game, where two players take turns removing prime numbers and their multiples from a set of consecutive integers. The goal is to determine the winner of multiple rounds.

- The solution uses the Sieve of Eratosthenes algorithm to efficiently find prime numbers within the given range for each round. The winner of each round is determined based on whether the count of prime numbers is odd or even. If the count is odd, the first player (Maria) wins; if even, the second player (Ben) wins. The overall winner is the player who wins the most rounds.
