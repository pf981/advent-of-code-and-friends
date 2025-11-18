with open("./2025/input/everybody_codes_e2025_q12_p1.txt") as f:
    lines = f.read().splitlines()

# grid = [int(x) for x in line] for line in lines]
m = {(r, c): int(ch) for r, line in enumerate(lines) for c, ch in enumerate(line)}
import collections

q = collections.deque([(0, 0)])
destroyed = set()
while q:
    r, c = q.popleft()
    if (r, c) in destroyed:
        continue
    destroyed.add((r, c))

    val = m[(r, c)]
    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc
        if (r2, c2) not in m or (r2, c2) in destroyed:
            continue
        if m[(r2, c2)] > val:
            continue
        q.append((r2, c2))

answer1 = len(destroyed)
print(answer1)
