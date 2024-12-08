with open("./2024/input/everybody_codes_e2024_q17_p1.txt") as f:
    lines = f.read().splitlines()

# lines = '''*...*
# ..*..
# .....
# .....
# *.*..'''.splitlines()

nodes = []
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == '*':
            nodes.append((r, c))

n_nodes = len(nodes)
edges = [] # d, i, j
for i in range(n_nodes):
    for j in range(n_nodes):
        if i == j:
            continue
        r1, c1 = nodes[i]
        r2, c2 = nodes[j]
        d = abs(r2 - r1) + abs(c2 - c1)
        edges.append((d, i, j))

edges.sort()

parents = [i for i in range(n_nodes)]

def union(i, j):
    parents[find(i)] = find(j)

def find(i):
    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]
    return i

total_distance = 0
for d, i, j in edges:
    if find(i) == find(j):
        continue
    union(i, j)
    total_distance += d

answer1 = total_distance + n_nodes
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q17_p2.txt") as f:
    lines = f.read().splitlines()


nodes = []
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == '*':
            nodes.append((r, c))

n_nodes = len(nodes)
edges = [] # d, i, j
for i in range(n_nodes):
    for j in range(n_nodes):
        if i == j:
            continue
        r1, c1 = nodes[i]
        r2, c2 = nodes[j]
        d = abs(r2 - r1) + abs(c2 - c1)
        edges.append((d, i, j))

edges.sort()

parents = [i for i in range(n_nodes)]

def union(i, j):
    parents[find(i)] = find(j)

def find(i):
    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]
    return i

total_distance = 0
for d, i, j in edges:
    if find(i) == find(j):
        continue
    union(i, j)
    total_distance += d

answer2 = total_distance + n_nodes
print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q17_p3.txt") as f:
    lines = f.read().splitlines()

nodes = []
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == '*':
            nodes.append((r, c))

n_nodes = len(nodes)
edges = [] # d, i, j
for i in range(n_nodes):
    for j in range(n_nodes):
        if i == j:
            continue
        r1, c1 = nodes[i]
        r2, c2 = nodes[j]
        d = abs(r2 - r1) + abs(c2 - c1)
        edges.append((d, i, j))

edges.sort()

distances = [0 for _ in range(n_nodes)]
parents = [i for i in range(n_nodes)]

def union(i, j, d):
    i = find(i)
    j = find(j)
    distances[j] += distances[i] + d
    distances[i] = 0
    parents[i] = j

def find(i):
    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]
    return i

for d, i, j in edges:
    if find(i) == find(j) or d >= 6:
        continue
    union(i, j, d)

import collections
import math

combined_distances = collections.Counter()
counts = collections.Counter()
for i, d in enumerate(distances):
    i = find(i)
    combined_distances[i] += d
    counts[i] += 1

sizes = []
for d, count in zip(combined_distances.values(), counts.values()):
    sizes.append(d + count)

sizes.sort()
answer3 = math.prod(sizes[-3:])
print(answer3)
