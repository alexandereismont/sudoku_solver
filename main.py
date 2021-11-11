from math import sqrt

import numpy as np

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
input_grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
              [5, 2, 0, 0, 0, 0, 0, 0, 0],
              [0, 8, 7, 0, 0, 0, 0, 3, 1],
              [0, 0, 3, 0, 1, 0, 0, 8, 0],
              [9, 0, 0, 8, 6, 3, 0, 0, 5],
              [0, 5, 0, 0, 9, 0, 6, 0, 0],
              [1, 3, 0, 0, 0, 0, 2, 5, 0],
              [0, 0, 0, 0, 0, 0, 0, 7, 4],
              [0, 0, 5, 2, 0, 6, 3, 0, 0]]

grid_sqrt = int(sqrt(len(input_grid)))


def print_input_grid():
    print("Input grid: \n{}".format(np.matrix(input_grid)))


def is_valid_row(grid: list[list[int]], i: int, number: int):
    return number not in grid[i]


# for x in input_grid[i]:
#    print(x)

def is_valid_column(grid: list[list[int]], j: int, number: int):
    column = []
    for x in range(9):
        column.insert(x, grid[x][j])
    return number not in column


def is_valid_box(grid: list[list[int]], i: int, j: int, number: int):
    grid_row_start = i - i % grid_sqrt
    grid_column_start = j - j % grid_sqrt
    for x in range(grid_row_start, grid_row_start + grid_sqrt):
        for y in range(grid_column_start, grid_column_start + grid_sqrt):
            if grid[x][y] == number:
                return False
    return True


def find_empty(grid: list[list[int]], length: int):
    for i in range(length):
        for j in range(length):
            if grid[i][j] == 0:
                return i, j
    return ()  # empty tuple


def solve_sudoku(grid: list[list[int]], length: int):
    pos: tuple[int, int] = find_empty(grid, length)
    if not pos:
        return True

    for x in range(1, length + 1):
        if is_valid_column(grid, pos[1], x) & is_valid_row(grid, pos[0], x) & is_valid_box(grid, pos[0], pos[1], x):
            grid[pos[0]][pos[1]] = x
            if solve_sudoku(grid, length):
                return True
            else:
                grid[pos[0]][pos[1]] = 0
    return False


if __name__ == '__main__':
    print_input_grid()
    solve_sudoku(input_grid, len(input_grid))
    print_input_grid()
