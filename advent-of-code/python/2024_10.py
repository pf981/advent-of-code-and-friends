from aocd import get_data, submit
import collections

inp = get_data(day=10, year=2024)
lines = [[int(x) for x in line] for line in inp.splitlines()]

nrows = len(lines)
ncols = len(lines[0])

def score(r, c, is_part2=False):
    q = collections.deque([(r, c)])
    result = 0
    seen = set()
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()

            if lines[r][c] == 9:
                result += 1
                continue
            for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                r2 = r + dr
                c2 = c + dc
                if not (0 <= r2 < nrows) or not (0 <= c2 < ncols) or lines[r2][c2] != lines[r][c] + 1:
                    continue
                if not is_part2 and (r2, c2) in seen:
                    continue
                seen.add((r2, c2))
                q.append((r2, c2))
    return result

answer1 = 0
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch != 0:
            continue
        answer1 += score(r, c)
print(answer1)

submit(answer1, part='a', day=10, year=2024)


# Part 2


answer2 = 0
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch != 0:
            continue
        answer2 += score(r, c, True)
print(answer2)

submit(answer2, part='b', day=10, year=2024)
