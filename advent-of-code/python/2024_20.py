from aocd import get_data, submit
import collections


def get_saves(time_from_start, min_savings, duration):
    result = 0
    for (r,c), t in time_from_start.items():
        for (r2, c2), t2 in time_from_start.items():
            if (r, c) == (r2, c2):
                continue
            d = abs(r - r2) + abs(c - c2)
            if d <= duration:
                result += t2 - t - d >= min_savings
    return result


inp = get_data(day=20, year=2024)
lines = inp.splitlines()

nrows = len(lines)
ncols = len(lines[0])

start = end = None
for row, line in enumerate(lines):
    for col, ch in enumerate(line):
        if ch == 'S':
            start = (row, col)
        elif ch == 'E':
            end = (row, col)

q = collections.deque([start]) # (r, c)
d = 1
time_from_start = {start: 0} # (r, c) -> t
while end not in time_from_start:
    for _ in range(len(q)):
        r, c = q.popleft()

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if lines[r2][c2] == '#':
                continue
            if (r2, c2) in time_from_start:
                continue
            time_from_start[(r2, c2)] = d
            q.append((r2, c2))
    d += 1


answer1 = get_saves(time_from_start, 100, 2)
print(answer1)

submit(answer1, part='a', day=20, year=2024)


# Part 2


answer2 = get_saves(time_from_start, 100, 20)
print(answer2)

submit(answer2, part='b', day=20, year=2024)
