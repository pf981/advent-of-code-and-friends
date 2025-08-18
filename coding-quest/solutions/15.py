import collections

import downloader

lines = downloader.get_puzzle(15).splitlines()

grid = [[int(s) for s in line.split()] for line in lines]
nrows = len(grid)
ncols = len(grid[0])

parents = {(r, c): (r, c) for r in range(nrows) for c in range(ncols) if grid[r][c]}


def union(i: tuple[int, int], j: tuple[int, int]):
    i = find(i)
    j = find(j)

    if i == j:
        return

    parents[i] = j


def find(i: tuple[int, int]) -> tuple[int, int]:
    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]
    return i


for i in parents:
    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        j = (i[0] + dr, i[1] + dc)

        if j not in parents:
            continue

        union(i, j)

groups = collections.defaultdict(int)
for i in parents:
    groups[find(i)] += grid[i[0]][i[1]]

answer = sum(groups.values()) // len(groups)
print(answer)
