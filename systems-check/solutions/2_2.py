import heapq

with open("./input/2.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])

valid = set()
high_cost = set()
for r in range(nrows):
    for c in range(ncols):
        ch = lines[r][c]

        if ch == "#":
            for dr, dc in [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]:
                r2 = r + dr
                c2 = c + dc
                high_cost.add((r2, c2))
        else:
            valid.add((r, c))

        if ch == "*":
            target = (r, c)

heap = [(0, 0, 0)]  # [(cost, r, c), ...]
seen = set()
d = 0
while heap:
    cost, r, c = heapq.heappop(heap)

    if (r, c) in seen:
        continue
    seen.add((r, c))

    if (r, c) == target:
        break

    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc

        if (r2, c2) not in valid or (r2, c2) in seen:
            continue

        cost2 = cost + 1 + ((r, c) in high_cost)
        heapq.heappush(heap, (cost2, r2, c2))


answer = cost
print(answer)
