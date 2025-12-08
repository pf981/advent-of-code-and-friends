from aocd import get_data, submit
import math
import collections
import heapq

inp = get_data(day=8, year=2025)
n_connections = 1000

# inp = """162,817,812
# 57,618,57
# 906,360,560
# 592,479,940
# 352,342,300
# 466,668,158
# 542,29,236
# 431,825,988
# 739,650,466
# 52,470,668
# 216,146,977
# 819,987,18
# 117,168,530
# 805,96,715
# 346,949,466
# 970,615,88
# 941,993,340
# 862,61,35
# 984,92,344
# 425,690,689"""
# n_connections = 10

lines = inp.splitlines()

positions = [tuple(int(x) for x in line.split(",")) for line in lines]
n = len(positions)

parents = {}
for pos in positions:
    parents[pos] = pos


def union(i, j):
    i = find(i)
    j = find(j)
    if i == j:
        return False
    parents[i] = j
    return True


def find(i):
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
connections_x = 0
for _, p1, p2 in distances:
    if union(p1, p2):
        # print(f"{p1=} {p2=}")
        connections_x = p1[0] * p2[0]
        connections += 1
    # else:
    #     connections += 1
    # if connections == n_connections:
    #     break

# groups = collections.Counter()
# for p in parents:
#     groups[find(p)] += 1

# print(heapq.nlargest(3, groups.values()))
answer2 = connections_x

# answer1 = math.prod(groups.values())
print(answer2)
submit(answer2, part="b", day=8, year=2025)

# 1000 not right
