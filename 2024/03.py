import collections


with open("./2024/input/everybody_codes_e2024_q03_p1.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

seen = set()

q = collections.deque()
for r in range(nrows):
    for c in range(ncols):
        if lines[r][c] == '.':
            seen.add((r, c))
            q.append((r, c))

d = 0
answer1 = 0
while q:
    answer1 += d * len(q)
    for _ in  range(len(q)):
        r, c = q.popleft()
        print(f'{d=} {r=} {c=}')
        
        for dr, dc in directions:
            r2 = r + dr
            c2 = c + dc
            if (r2, c2) in seen or not (0 <= r2 < nrows) or not (0 <= c2 < ncols):
                continue
            seen.add((r2, c2))
            q.append((r2, c2))
    d += 1

print(answer1)


with open("./2024/input/everybody_codes_e2024_q03_p2.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])

directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

seen = set()

q = collections.deque()
for r in range(nrows):
    for c in range(ncols):
        if lines[r][c] == '.':
            seen.add((r, c))
            q.append((r, c))

d = 0
answer2 = 0
while q:
    answer2 += d * len(q)
    for _ in  range(len(q)):
        r, c = q.popleft()
        print(f'{d=} {r=} {c=}')
        
        for dr, dc in directions:
            r2 = r + dr
            c2 = c + dc
            if (r2, c2) in seen or not (0 <= r2 < nrows) or not (0 <= c2 < ncols):
                continue
            seen.add((r2, c2))
            q.append((r2, c2))
    d += 1


print(answer2)


import collections
with open("./2024/input/everybody_codes_e2024_q03_p3.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

seen = set()

q = collections.deque()
for r in range(nrows):
    for c in range(ncols):
        if lines[r][c] == '.':
            seen.add((r, c))
            q.append((r, c))

for r in range(nrows):
    q.append((r, -1))
    q.append((r, ncols))
for c in range(ncols):
    q.append((-1, c))
    q.append((nrows, c))

d = 0
answer3 = 0
while q:
    answer3 += d * len(q)
    for _ in  range(len(q)):
        r, c = q.popleft()
        # print(f'{d=} {r=} {c=}')
        
        for dr, dc in directions:
            r2 = r + dr
            c2 = c + dc
            if (r2, c2) in seen or not (0 <= r2 < nrows) or not (0 <= c2 < ncols):
                continue
            seen.add((r2, c2))
            q.append((r2, c2))
    d += 1

print(answer3)
