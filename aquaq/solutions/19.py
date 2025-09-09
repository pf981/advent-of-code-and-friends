import functools
import itertools


@functools.cache
def step(on: frozenset[tuple[int, int]], n: int) -> frozenset[tuple[int, int]]:
    on2 = set()
    for r in range(n):
        for c in range(n):
            neighbors = 0
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                r2 = r + dr
                c2 = c + dc
                neighbors += (r2, c2) in on

            if neighbors % 2 == 1:
                on2.add((r, c))
    return frozenset(on2)


with open("./input/19.txt") as f:
    text = f.read()

answer = 0
for line in text.splitlines():
    steps, n, *points = (int(x) for x in line.split())

    on_mut = set()
    for r, c in itertools.batched(points, 2):
        on_mut.add((r, c))

    on = frozenset(on_mut)

    for _ in range(steps):
        on = step(on, n)
    answer += len(on)

print(answer)
