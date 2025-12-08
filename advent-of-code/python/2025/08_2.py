from aocd import get_data, submit

inp = get_data(day=8, year=2025)
N_CONNECTIONS = 1000

lines = inp.splitlines()

positions = [tuple(int(x) for x in line.split(",")) for line in lines]
n = len(positions)

parents = {}
for pos in positions:
    parents[pos] = pos

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

answer2 = None
for _, p1, p2 in distances:
    if union(p1, p2):
        answer2 = p1[0] * p2[0]

submit(answer2, part="b", day=8, year=2025)
