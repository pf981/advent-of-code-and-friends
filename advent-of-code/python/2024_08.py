
from aocd import get_data, submit
import collections

inp = get_data(day=8, year=2024)
lines = inp.splitlines()

nrows = len(lines)
ncols = len(lines[0])

m = collections.defaultdict(list)
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c != '.':
            m[c].append((row, col))

antinodes = set() # (r, c)
for ch, positions in m.items():
    for r, c in positions:
        for r2, c2 in positions:
            if r == r2:
                continue
            dr = r2 - r
            dc = c2 - c
            r3 = r2 + dr
            c3 = c2 + dc
            if 0 <= r3 < nrows and 0 <= c3 < ncols:
                antinodes.add((r3, c3))

answer1 = len(antinodes)
print(answer1)

submit(answer1, part='a', day=8, year=2024)


# Part 2


antinodes = set() # (r, c)
for ch, positions in m.items():
    for r, c in positions:
        for r2, c2 in positions:
            if (r, c) == (r2, c2):
                continue

            # Handle vertical line even though it isn't present in the data
            if c2 - c == 0:
                for r3 in range(nrows):
                    antinodes.add((r3, c))
                continue

            # slope = dr / dc
            # y - y1 = slope * (x - x1)
            # row = slope * (c3 - c) + r
            for c3 in range(ncols):
                if (dr * (c3 - c)) % dc != 0:
                    continue

                r3 = dr * (c3 - c) // dc + r
                if 0 <= r3 < nrows and 0 <= c3 < ncols:
                    antinodes.add((r3, c3))

answer2 = len(antinodes)
print(answer2)

submit(answer2, part='b', day=8, year=2024)
