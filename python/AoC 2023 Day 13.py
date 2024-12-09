from aocd import get_data

inp = get_data(day=13, year=2023)

from aocd import get_data, submit


def is_mirror(grid, col):
    for line in grid:
        if any(a != b for a, b in zip(line[:col][::-1], line[col:])):
            return False
    return True


def get_mirror_cols(grid):
    return {col for col in range(1, len(grid[0])) if is_mirror(grid, col)}


def get_mirror_rows(grid):
    grid = list(zip(*grid))[::-1]
    return {row for row in range(1, len(grid[0])) if is_mirror(grid, row)}


inp = get_data(day=13, year=2023)
grids = [grid.splitlines() for grid in inp.split('\n\n')]
answer1 = 0
for grid in grids:
    mirror_cols = get_mirror_cols(grid)
    mirror_rows = get_mirror_rows(grid)
    answer1 += next(iter(mirror_cols), 0) + 100 * next(iter(mirror_rows), 0)

print(answer1)

submit(answer1, part='a', day=13, year=2023)


# Part 2


import itertools


answer2 = 0
for grid_original in grids:
    for row, col in itertools.product(range(len(grid_original)), range(len(grid_original[0]))):
        grid = [list(s)for s in grid_original]
        grid[row][col] = {'#': '.', '.': '#'}[grid[row][col]]

        mirror_cols = get_mirror_cols(grid).difference(get_mirror_cols(grid_original))
        mirror_rows = get_mirror_rows(grid).difference(get_mirror_rows(grid_original))

        if len(mirror_cols) + len(mirror_rows) == 1:
            answer2 += next(iter(mirror_cols), 0) + 100 * next(iter(mirror_rows), 0)
            break

print(answer2)

submit(answer2, part='b', day=13, year=2023)
