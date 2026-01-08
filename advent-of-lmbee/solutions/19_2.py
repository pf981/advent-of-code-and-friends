import functools
import math


def get_max_sum(grid: list[list[int]]) -> int:
    @functools.cache
    def get_max_part(r: int, c: int, dr: int, dc: int) -> int:
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
            return 0
        return grid[r][c] + max(
            get_max_part(r + dr, c, dr, dc),
            get_max_part(r, c + dc, dr, dc),
        )

    result = 0
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            # robot1: Down, (Collide), Down
            # robot2: Right, (Collide), Right
            option1 = (
                get_max_part(r - 1, c, -1, -1)  # robot1 before collision
                + get_max_part(r + 1, c, 1, 1)  # robot1 after collision
                + get_max_part(r, c - 1, 1, -1)  # robot2 before collision
                + get_max_part(r, c + 1, -1, 1)  # robot2 after collision
            )

            # robot1: Right, (Collide), Right
            # robot2: Up, (Collide), Up
            option2 = (
                get_max_part(r, c - 1, -1, -1)  # robot1 before collision
                + get_max_part(r, c + 1, 1, 1)  # robot1 after collision
                + get_max_part(r + 1, c, 1, -1)  # robot2 before collision
                + get_max_part(r - 1, c, -1, 1)  # robot2 after collision
            )

            sum_ = 2 * grid[r][c] + max(option1, option2)
            result = max(result, sum_)
    return result


with open("data/day19.txt") as f:
    text = f.read()

grids = [
    [[int(x) for x in line] for line in grid.splitlines()]
    for grid in text.split("\n\n")
]

sums = [get_max_sum(grid) for grid in grids]
answer = math.prod(sums)
print(answer)
