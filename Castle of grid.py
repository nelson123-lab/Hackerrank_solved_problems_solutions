from collections import deque
import math
import os
import random
import re
import sys


def minimumMoves(grid, startX, startY, goalX, goalY):
    visited = set()
    queue = deque([[startX, startY, 0]])

    while queue:
        x, y, moves_qty = queue.popleft()
        moves_qty += 1

        for edge_x, edge_y in get_edges(x, y):
            if (edge_x, edge_y) in visited:
                continue
            if goalX == edge_x and goalY == edge_y:
                return moves_qty

            visited.add((edge_x, edge_y))
            queue.append([edge_x, edge_y, moves_qty])
    
    return -1

def get_edges(x, y):
    """
    The hack is here. In a regular BFS algorithm we would only look for the neighbours.
    As we can move multiple cells in the same column or row with only one movement, we need
    to consider that extra movements, which is doing on the while statement.
    """
    moves = (
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0),
    )
    edges = []
    for move_x, move_y in moves:
        canMove = True
        edge_x, edge_y = x, y
        while canMove:

            edge_x, edge_y = edge_x + move_x, edge_y + move_y
            try:
                if grid[edge_x][edge_y] == '.':
                    edges.append((edge_x, edge_y))
                else:
                    canMove = False
            except IndexError:
                canMove = False
    
    return edges

if __name__ == '__main__':

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    print(result)
