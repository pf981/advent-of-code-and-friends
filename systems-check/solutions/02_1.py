import collections

with open("./input/2.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])
valid = {(r, c) for r in range(nrows) for c in range(ncols) if lines[r][c] != "#"}
target = next((r, c) for r in range(nrows) for c in range(ncols) if lines[r][c] == "*")

q = collections.deque([(0, 0)])
seen = {(0, 0)}
d = 0
while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        if (r, c) == target:
            break

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if (r2, c2) in valid and (r2, c2) not in seen:
                seen.add((r2, c2))
                q.append((r2, c2))

    else:
        d += 1
        continue
    break

answer = d
print(answer)
