from __future__ import annotations

import functools

path = input().strip()
path = "????U???????????D???????????????????????????????"
n = 7


@functools.lru_cache()
def count_ways(i: int, r: int, c: int, visited_mask: int) -> int:
    if i == len(path):
        return int((r, c) == (n - 1, 0))

    # Reached end prematurely
    if (r, c) == (n - 1, 0):
        return 0

    valid_directions = []
    for direction in "URDL":
        r2 = r + (direction == "D") - (direction == "U")
        c2 = c + (direction == "R") - (direction == "L")

        if not (0 <= r2 < n and 0 <= c2 < n):
            continue

        mask = 1 << (r2 * n + c2)
        if visited_mask & mask:
            continue

        valid_directions.append(direction)

    valid_directions = "".join(valid_directions)
    # Can only go left and right means we will cut off some cell
    if valid_directions in ("RL", "UD"):
        return 0

    ways = 0
    for direction in valid_directions:
        if path[i] != "?" and path[i] != direction:
            continue

        r2 = r + (direction == "D") - (direction == "U")
        c2 = c + (direction == "R") - (direction == "L")

        mask = 1 << (r2 * n + c2)
        ways += count_ways(i + 1, r2, c2, visited_mask | mask)

    return ways


print(count_ways(0, 0, 0, 1))
