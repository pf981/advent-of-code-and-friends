import collections

with open("./2026/input/everybody_codes_e2026_q17_p1.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])

q = collections.deque()
q.append((0, 0))
seen = {(0, 0)}
d = 0
while q:
    for _ in range(len(q)):
        r, c = q.popleft()

        if (r, c) == (nrows - 1, ncols - 1):
            break

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                continue
            if (r2, c2) in seen:
                continue
            if lines[r2][c2] != "#":
                continue
            seen.add((r2, c2))

            q.append((r2, c2))
    else:
        d += 1
        continue
    break

assert (r, c) == (nrows - 1, ncols - 1)
answer = d
print(answer)
