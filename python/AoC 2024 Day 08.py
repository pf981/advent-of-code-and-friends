
from aocd import get_data, submit
import collections

inp = get_data(day=8, year=2024)

inp = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
'''

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

# submit(answer1, part='a', day=8, year=2024)


# Part 2


inp = get_data(day=8, year=2024)

# inp = '''............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............
# '''
import math
# inp = '''T.........
# ...T......
# .T........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........
# ..........'''

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
            if (r, c) == (r2, c2):
                print(f'SAME {r, c=}')
                continue

            dr = r2 - r
            dc = c2 - c

            print(f'{dr=} {dc=}')
            if dc == 0:
                print(f'!!!')
                for r3 in range(nrows):
                    antinodes.add((r3, c))
                continue
            if dr == 0:
                print(f'??!!!')

            slope = dr / dc
            # y - y1 = slope * (x - x1)
            # row = slope * (c3 - c) + r


            for c3 in range(ncols):
                if (dr * (c3 - c)) % dc != 0:
                    continue

                r3 = dr * (c3 - c) // dc + r
                # if int(r3) != r3:
                # if not math.isclose(r3, int(r3)):
                #     continue
                r3 = int(r3)
                if 0 <= r3 < nrows and 0 <= c3 < ncols:
                # if 0 <= r3 < nrows and 0 <= c3 < ncols and lines[r3][c3] == '.':
                    antinodes.add((r3, c3))


            # for c3 in range(ncols):
            #     r3 = slope * (c3 - c) + r
            #     # if int(r3) != r3:
            #     if not math.isclose(r3, int(r3)):
            #         continue
            #     r3 = int(r3)
            #     if 0 <= r3 < nrows and 0 <= c3 < ncols:
            #     # if 0 <= r3 < nrows and 0 <= c3 < ncols and lines[r3][c3] == '.':
            #         antinodes.add((r3, c3))

# for row, line in enumerate(lines):
#     for col, c in enumerate(line):
#         if c == '.' and (row, col) in antinodes:
#             print('#', end='')
#         else:
#             print(c, end='')
#     print()

# all(pos in antinodes for poses in m.values() for pos in poses)
# import re
# all(re.match(r'^[a-zA-Z0-9]$', c) for c in m)


answer2 = len(antinodes)
print(answer2)

submit(answer2, part='b', day=8, year=2024)

# y = mx + b. Then just sub in integer x

for ch, positions in m.items():
    print(ch, len(positions))

# 1307
# >>> submit(answer2, part='b', day=8, year=2024)
# That's not the right answer.  
# If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, 
# or you can ask for hints on the subreddit.  Please wait one minute before trying again. [Return to Day 8]