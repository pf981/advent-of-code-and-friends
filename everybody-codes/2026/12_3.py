import functools
import itertools

with open("./2026/input/everybody_codes_e2026_q12_p3.txt") as f:
    lines = f.read().splitlines()

points = frozenset(
    (r, c) for r, line in enumerate(lines) for c, ch in enumerate(line) if ch == "#"
)


def get_points(
    r: int, c: int, points: frozenset[tuple[int, int]]
) -> frozenset[tuple[int, int]]:
    result = set()

    def dfs(r: int, c: int) -> None:
        if (r, c) in result or (r, c) not in points:
            return
        result.add((r, c))

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            dfs(r2, c2)

    dfs(r, c)
    return frozenset(result)


def normalise_points(points: frozenset[tuple[int, int]]) -> frozenset[tuple[int, int]]:
    if not points:
        return frozenset()
    top_left_r = min(r for r, _ in points)
    top_left_c = min(c for r, c in points if r == top_left_r)
    return frozenset((r - top_left_r, c - top_left_c) for r, c in points)


@functools.cache
def get_min_cost(points: frozenset[tuple[int, int]]) -> int:
    if not points:
        return 0

    # -
    remaining = set(points)
    for c in itertools.count():
        if (0, c) not in points:
            break
        remaining.remove((0, c))
    horizontal_cost = sum(get_min_cost(ps) for ps in break_shapes(frozenset(remaining)))

    # |
    remaining = set(points)
    for r in itertools.count():
        if (r, 0) not in points:
            break
        remaining.remove((r, 0))
    vertical_cost = sum(get_min_cost(ps) for ps in break_shapes(frozenset(remaining)))

    return 1 + min(horizontal_cost, vertical_cost)


def break_shapes(
    points: frozenset[tuple[int, int]],
) -> list[frozenset[tuple[int, int]]]:
    result = []
    seen = set()
    for r, c in points:
        if (r, c) in seen:
            continue

        ps = get_points(r, c, points)
        seen.update(ps)
        result.append(normalise_points(ps))
    return result


answer = sum(get_min_cost(ps) for ps in break_shapes(points))
print(answer)
