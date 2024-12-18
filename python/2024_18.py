from aocd import get_data, submit
import re
import collections


def solve(corrupted):
    seen = {(0, 0)}
    q = collections.deque([(0, 0, (0, 0))])
    d = 0
    while q:
        for _ in range(len(q)):
            x, y, path = q.popleft()
            if (x, y) == (70, 70):
                return d
            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                x2 = x + dx
                y2 = y + dy
                if not (0 <= x2 <= max_x) or not (0 <= y2 <= max_y) or (x2, y2) in seen or (x2, y2) in corrupted:
                    continue
                seen.add((x2, y2))
                q.append((x2, y2, path + ((x2, y2),)))
        d += 1
    return None


inp = get_data(day=18, year=2024)

max_x = max_y = 70
first_n = 1024
lines = inp.splitlines()

corrupted = set()
for i, line in enumerate(lines):
    if i == first_n:
        break
    xx, yy = map(int, re.findall(r'-?[0-9]+', line))
    corrupted.add((xx, yy))

answer1 = solve(corrupted)
print(answer1)

submit(answer1, part='a', day=18, year=2024)


# Part 2


for line in lines[1025:]:
    xx, yy = map(int, re.findall(r'-?[0-9]+', line))
    corrupted.add((xx, yy))
    if not solve(corrupted):
        answer2 = f'{xx},{yy}'
        break
print(answer2)

submit(answer2, part='b', day=18, year=2024)
