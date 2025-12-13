from __future__ import annotations

import functools


reserved = {
    (r, c) for r, line in enumerate(open(0)) for c, ch in enumerate(line) if ch == "*"
}


@functools.lru_cache()
def count_ways(
    r: int,
    diags1: frozenset[int],
    diags2: frozenset[int],
    cols: frozenset[tuple[int, int]],
) -> int:
    if r == 8:
        return 1

    ways = 0
    for c in range(8):
        if (r, c) in reserved:
            continue
        if c in cols:
            continue

        diag1 = r - c
        diag2 = r + c
        if diag1 in diags1 or diag2 in diags2:
            continue

        ways += count_ways(r + 1, diags1 | {diag1}, diags2 | {diag2}, cols | {c})

    return ways


print(count_ways(0, frozenset(), frozenset(), frozenset()))
