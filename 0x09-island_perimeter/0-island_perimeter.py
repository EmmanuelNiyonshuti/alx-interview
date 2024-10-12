#!/usr/bin/python3
'''
comprises a function that finds the perimeter of an island.
'''


def island_perimeter(grid):
    '''
    finds island perimeter.
    Args:
        grid (list) - nested list representing a grid.
    Return:
        int - island perimeter.
    '''
    if not grid:
        return
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 1
                if r < rows - 1 and grid[r+1][c] == 1:
                    perimeter -= 1
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 1
                if c < cols-1 and grid[r][c+1] == 1:
                    perimeter -= 1
    return perimeter
