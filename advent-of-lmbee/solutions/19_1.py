import functools
import math


def get_max_sum(grid: list[list[int]]) -> int:
    @functools.cache
    def get_max_part(r: int, c: int) -> int:
        if (r, c) == (len(grid) - 1, len(grid[0]) - 1):
            return grid[r][c]

        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
            return 0

        return grid[r][c] + max(get_max_part(r + 1, c), get_max_part(r, c + 1))

    return get_max_part(0, 0)


with open("data/day19.txt") as f:
    text = f.read()

grids = [
    [[int(x) for x in line] for line in grid.splitlines()]
    for grid in text.split("\n\n")
]

sums = [get_max_sum(grid) for grid in grids]
answer = math.prod(sums)
print(answer)
