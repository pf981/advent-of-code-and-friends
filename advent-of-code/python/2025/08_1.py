import collections
import heapq
import math

from aocd import get_data, submit


inp = get_data(day=8, year=2025)
N_CONNECTIONS = 1000

lines = inp.splitlines()


positions = [tuple(int(x) for x in line.split(",")) for line in lines]
n = len(positions)

parents = {}
sizes = {}
for pos in positions:
    parents[pos] = pos
    sizes[pos] = 1

P = tuple[int, int, int]


def union(i: P, j: P) -> bool:
    i = find(i)
    j = find(j)
    if i == j:
        return False
    parents[i] = j
    return True


def find(i: P) -> P:
    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]
    return i


distances = []  # d, p1, p2
for i in range(n):
    for j in range(i + 1, n):
        x1, y1, z1 = positions[i]
        x2, y2, z2 = positions[j]
        d = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
        distances.append((d, positions[i], positions[j]))

distances.sort()

connections = 0
for i in range(N_CONNECTIONS):
    _, p1, p2 = distances[i]
    union(p1, p2)

groups = collections.Counter()
for p in parents:
    groups[find(p)] += 1

answer1 = math.prod(heapq.nlargest(3, groups.values()))
submit(answer1, part="a", day=8, year=2025)
