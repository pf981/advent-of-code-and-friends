import heapq

with open("./input/2026/08/input2.txt") as f:
    text = f.read()

target, *grid = text.splitlines()
targets = {}  # (r, c) -> id_
for part in target.split(","):
    id_, r, c = map(int, part.split())
    assert (r, c) not in targets
    targets[(r, c)] = id_

nrows = len(grid)
ncols = len(grid[0])
heap = []  # [(d, turns, heading, r, c), ...]
for heading in "NESW":
    heapq.heappush(heap, (0, 0, heading, 0, 0))

seen = set()
order = []  # [(id_, turns), ...]
while heap:
    d, turns, heading, r, c = heapq.heappop(heap)

    if (r, c) in targets:
        order.append((targets[(r, c)], turns))
        del targets[(r, c)]

    if (heading, r, c) in seen:
        continue
    seen.add((heading, r, c))

    for heading2 in "NESW":
        r2 = r + (heading2 == "S") - (heading2 == "N")
        c2 = c + (heading2 == "E") - (heading2 == "W")
        if not (0 <= r2 < nrows and 0 <= c2 < ncols):
            continue
        if grid[r2][c2] == "#":
            continue
        heapq.heappush(heap, (d + 1, turns + (heading2 != heading), heading2, r2, c2))

answer = " ".join(map(str, order[0] + order[-1]))
print(answer)
