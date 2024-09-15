#!/usr/bin/python3
""" nqueens algorithm """
import sys


def safe_place_queen(board, row, col, N):
    """ finds a safe place to place a queen """
    for i in range(row):
        if board[i] == col:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i] == j:
            return False
    return True


def nqueens(N):
    def backtrack(row):
        """
        backtracks when current row's columns are exhausted
        with no safe place for a queen.
        """
        if row == N:
            result.append([[i, board[i]] for i in range(N)])
            return
        for col in range(N):
            if safe_place_queen(board, row, col, N):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1
    board = [-1] * N
    result = []
    backtrack(0)
    return result


if __name__ == "__main__":
    if not len(sys.argv) == 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except(ValueError, TypeError):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    sol = nqueens(n)
    for i in sol:
        print(i)
