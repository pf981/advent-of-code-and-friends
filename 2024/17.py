import collections
import math


class UnionFind:
    def __init__(self, n_nodes: int) -> None:
        self.distances = [0 for _ in range(n_nodes)]
        self.parents = [i for i in range(n_nodes)]

    def union(self, i: int, j: int, d: int) -> None:
        i = self.find(i)
        j = self.find(j)
        self.distances[j] += self.distances[i] + d
        self.distances[i] = 0
        self.parents[i] = j
    
    def find(self, i: int) -> int:
        while self.parents[i] != i:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
        return i
    
    def get_sizes(self) -> list[int]:
        combined_distances = collections.Counter()
        counts = collections.Counter()
        for i, d in enumerate(self.distances):
            i = self.find(i)
            combined_distances[i] += d
            counts[i] += 1

        sizes = []
        for d, count in zip(combined_distances.values(), counts.values()):
            sizes.append(d + count)

        sizes.sort()
        return sizes


def parse(lines: list[str]) -> tuple[list[tuple[int, int, int]], int]:
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

    return edges, n_nodes


with open("./2024/input/everybody_codes_e2024_q17_p1.txt") as f:
    lines = f.read().splitlines()

edges, n_nodes = parse(lines)
uf = UnionFind(n_nodes)

for d, i, j in edges:
    if uf.find(i) == uf.find(j):
        continue
    uf.union(i, j, d)

answer1 = uf.get_sizes()[0]
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q17_p2.txt") as f:
    lines = f.read().splitlines()

edges, n_nodes = parse(lines)
uf = UnionFind(n_nodes)

for d, i, j in edges:
    if uf.find(i) == uf.find(j):
        continue
    uf.union(i, j, d)

answer2 = uf.get_sizes()[0]
print(answer2)


# Part 3



with open("./2024/input/everybody_codes_e2024_q17_p3.txt") as f:
    lines = f.read().splitlines() 

edges, n_nodes = parse(lines)
uf = UnionFind(n_nodes)

for d, i, j in edges:
    if uf.find(i) == uf.find(j) or d >= 6:
        continue
    uf.union(i, j, d)

answer3 = math.prod(uf.get_sizes()[-3:])
print(answer3)
