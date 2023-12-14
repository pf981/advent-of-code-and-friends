# Databricks notebook source
#%pip install z3-solver

# COMMAND ----------

inp = '''O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
'''

# COMMAND ----------

inp = '''...#O#O#.#...O...O...##...#..O#OO..OO....#.#OO....#.#.......O..O.#..#O.#......#.OO.....#....OO#....#
.#.##......O.O.#..#.OO..........#O.#....O.#..O............#.O.......#....OO.#.#..#O.O..#....O....O..
.#OO......O.O.O#O.#.##.....O...O....#O.O.OO.....OO...O..#O..O...O..#...O.#...#.....#O......O.....#..
O...##OO..O.O..##...O#..O#O.......#.OO..#....#...#.O....#.O..#O..#O...O.###.#....#.#..##.#...O...#.#
...#.#.....#....#O#...#..OO...#..#.......O.O..O##....O#.OOOOO.##.....O..#.O.OO..O.....O....#.O....OO
O#......O..#O##O........OO..#......#...#O..O..##.............O..#........O...##OOO.###O.O.##.O.#.O.O
.#O...OOO...#..O#.#.O.O..........#.O#..#.#....OO#O##.#...OO....#O.OO..#......#.......#...O..#.O.O##.
.#......#O..O..#..#.#.........O...#.#........O.#...O....#.O...#.......O#.O..#.#.....O...##....#.#O..
#..O..#OO...O##......#........O....O#..O.O..OO.OO....##O.OO...O##.#OO#...O..#..O....O.O.O.O...O.OO..
....##.O..OO.#.....##.#O#O.O.#..#...#..OO#......OO.......O.O.O.O..##..O.##......O...O.#..O...O.O.###
.O.#O......O.O.#....#......O#.......O......O#.O...#...O...#..#.#..#...##.#..##...O#O#.O.#.#...#.#.O.
#O.O....##....#..O.###..O.......OOOO#O#O.#OO.##...OO.O#........O..#OO.#.#...O.O.O....O....#O.##...#O
.OOO...O....#O.#....#..O#..OO.....#.#......#OO..#........O.O.O.....#....O.O#.O.....O.OO.##O..O##....
...O#....#O...O..##..O.#..O#..OOOO#..OOO.#O#..#OO.O...O..#.#..#..#..#O..O.OO..O...O.O..OO...........
..OO###..##..#.....O....O.....O.#O.......O..O..##...O#...O#..#...O..O....O#.O##..............#....O#
.##.###.....###O....O.O..O...O.O..O.#......#O.#..O.O#.#O##O..O#.....O.#...........O..O....O...O.O...
...O.................#...........#.O.......O.....#..O.O.O.....O........##.OOO.#.....O.OO...........#
..O.O#...#O...O.#....#.OO..#O..#.....#.##.....OO....O..O...#...#..OO..O.O....#OO........#O.##....O..
O..#..O.#.O....O..#OO##.OO...O.##O..#..#.##..O#.#.OO.O........O....#O.OO.O.#O.O.#...##O##..OO..#.O..
...#.O#..........O###...#.O.#.O#.#.OO...OO#...O.....O..O..#.OO.....##...O#........#.O.O......#.O....
OO#..O.##..##OO..#....O..#.O..#..O.#...#O#.O..O###....O#O#.#..O#.##.#......#.....O..OO..........#O..
#O.##..#.....###.#O#...#O.##....#...O..#..#..##...#.#..#.#O...O.#.#O....##O..O.O...O.#.OO.##..O#.O..
#O#.....#O.....#.##.O..O....#..O.........#....#.O#.O..........#...O.O#..#.O.#....#.O..O.O#O.O.#O.#..
.O#.O..O#...#......O..#O#.O#....#...###.#.#.##.O#...#..#O#O.O...#.#...O...##.O#.#O.....O....O.......
O........O....##..##.OO.....OO...O..#..O#...O..O..OOO...O...O......#..##....O.#...O#O............#..
..#OO.OO.O..##...#........O......O.#O..O#.#O#.#...#.#...O.O....O......#....#.#..#.#............#..OO
...##O.O.......#...#O#..OO..O.O.#.#..##.........O##O..O..O#..O#.#O..O...O.......##OO..OO..#O..###O#.
.....#..O..........O.....O#...O.O#....#O#...O..#.#O#....#.#O......O....##......O..OOO#O...#...##O..#
......O##...OO.OO#.OO#..#...#...#.#...#OO...O.......#..O.O.O.##..#......O##....#......OO.#O..#O.O...
....OO....O##..O..O.O.......#....O.O....#.OO...O..#O.#..#.#O.#.....O..#.OO.OO..#....O.....O.O#O...O.
OOOO.O.#.#O#.O.........#O..O#O...O.#..#...O...O.OO..OO...#O#.##O.O.#...OO##...O..##OO..#O...O..O.OOO
#O.O.#.O.OO.O...#O#.#O.OO..O#O...O###....O....O.O.O.....O...#.OO.##....O.O..#......#..#O.O##...#.O#.
O#......O.#...O.....O.O..#.##.OO...O...O.......O.O.#...#OO..OO...OO..O.##.O...#O#.O........OO#....##
OO......O#.#..O...O...O..##O...O.###..O..OO...OO..O.#O...#.#...O.#.OO.......#.##...O......O#.....O..
.#..##.....OO...O...O..#.......O.O.#....O..#...O....O..O#...OO.......O...O.O.#..O.O....O.O.#.O.O.OO.
....O....O.#O#....#O#O..O.....#..#.O.O.O..O...O.O..O...O..#O#....O.O.............O..O...O....O......
..#.O....OOOO#OO#.#.O..O....O....O.#.#..O....#.O#.O......O...#.............O##.......#....O..######.
......OO##O..##O#.....O..OO.#..#O..##..#.O#........O.O...##OO......OO.#.#...#.OO...O.OO......O.O...#
OO..O....O..#.#.O#..O#O...###.O#.....O...##....OOO...#O..O..#OO.O#....##.O..O.........OOO.........O#
..O.O.O#O...OO..##....#.#...O...#.##.......##...#O.#O..#...##.....O.....OOO..O...O......#...OO...#.O
#O...OO.........OO.O....#OO......O##.O..##....O..#.O.O.O#.O.OO#O..O...#.#...#.#...O.OO...##.....##.O
...OOOOO.O...O#.......OO#.O..OO..#OO......O...#..O##.#....O#....O.O...#.....##.O....#..##..O..#.....
.OO.....O#....#....#O..O..OO#OOO..O#.......#O#..O.O..O..O##..O.......OO.......O.##...O.O..#........O
....O#.O......#..O.OO...OO#.#..O#....O..O#.#..#...O#..OO...#O#.....O...O.....##.#..#O.O..O#OO.O.#O.O
..O.#.#.....O#.O.....OOOO.O..#..#O.#.#O.#OO.....O..#..O..O..#O......##O.#O..#.OOO....#O.O.#O...#..O.
......#.O...O.O#....OO#..O#....#..O...O.......#OO...#...##O#O##.O...O...O......O##.O.O#.#OO.OO.O#...
....O...O.O..#..O........O..OO...OO#...OO.......O#.OOO#...OO#OO#O.O.O#OO.....O.###O..O#.O...#.......
#O.#OO.....##O.O....O..O.OO.#...O...#.O.O..O.OOO#.....O....#.....O...##...#...#..#........#..#.O..O.
...O#......O..O.#.......#....#O...OOOO...O..O.O.O.#O....#.....O..#...O..#..O..............#O....OO..
OO....O.#..O.#..#.#OO#...OO...O.#O...OO......#..O#..O..O#O...#OOO#..#.O...##.......#.#OO.O.###.O...#
.OO...#.O...#O.O.....O...##.#..O.#O.O.....O..O.....##...OO...O..#O..........#OO.#......O#...O#...O..
.O.#.O.O..........O...O.#.##OO....##........O.#.....O#O...#.O.....OOO#..........#..O..#..O.#O.#..O..
.O..#.....#O......O....O....O....#..#.....O...O...OO#...O..#...O...#...O.##OO.#.O#.OOO#OO#...#....#.
.OOO#.....O.O.#.OO.........#O##.OO##O..#..#OO.OOOO...O..#.#..O#....OO..#...O#O....#OOO.#...O.#..#...
...O#...#..#.#...O.#O..#.......#...#...O#......#O.O.#.OO.O#O.O.#.O....##..O#O.##.#.....OO..O......O.
..#.#.O.O.#..O..#.O....OO....O##.O.#...#O...O.OO.O......#..O.....#........O.#......O.#.##..OO...OO.#
....O...##....OO#O#O..#.O.##..O....##OO....O..OOO..#O..#.O...#.......O#.......OO.O.#..#.OO.O..#OO...
.#.....#O#.#OO#.#.#O##.O#....#.....#.##..O...#.....O#.O.O...O.O....#........#O...#..OO..O.#.OOOOO.O#
O....#O......O...O..O#..#.O..O.OO.....#.O.OO.O...#O.OOO....O.........#....#.#.O.##.#O...O.O#O.O#..#.
.OO.O..OOOO#.#.......O..................O......#..#...O.#O#O.....#..O..#O.#..........##.#O#.O..##...
..O...O.OO#.O##.##.#O....O....#...#...O...OOO........O.O..#.##......###.........##...O..O...OO...O.#
OOOO......#.O..OO.OO#..#...O.##.#O..O#.OO#.......#.O.O.OO.O.#OO#O.#...#......O#O..O.O....#O##.O..O.#
.......O..O...OO.#O..O....O#..#.##.......O...........#..#.....O......#.#..O.......O.O#..#.O.#O.OOO#.
#.#.O...##.......O...O..O.#..#....O##......O.##OO......OO.....O.O.##.#....#...O....#O#.#....#.O#..#.
O.O......O#.....#...#..#.O#..##O..O#O......O.......##..O.....#O.O...O..#..O..O...#.O.#..O..#.O#.#.O.
.#...OO#.O#.#.O.O.O..OO....OO....O...O#.O.#......#.O#.OO#.O..O.OO.O.#.O...OO.....###O..#.O.....O.O#O
..##OO...#..##.O#.......#......#.......O..OO.....O...OO...#..O..O..O..OO.O.O.O......O#...O.#..O.O#..
...#.O..#...O.#.##.O.OO..OO.....#..#..O..#..O.#..O..OO..O.#.#...##......#...#O.#....#O#...OOO#...#..
.......#O...#......O..O...#..O..#....#.O..O.##........#.....O....O...#O#OOOOOO..O.....##..O..#O.O...
#.O...OOO..O.O.###.#..O..OO.O....O##...#.O....OO.......O..........##...O...#.#.OO.###...O..........O
#....O#OO.OO#O..............#.#.#...O#OO.##.#...O.O....O....#O.#..#......O.....O..O.O#O......OO....O
...O.OO....OO.O..O#O.O.O.....O.#.O.#..O....#.O#O.#.......OO....#.#.O...O.#.#..#O.O##..#.#...#....O#.
..#.O...OOO..O..#..O#.O....#O#O.O##....O.O.....O...........O#...##.....#....O....O.OOO#O..##O..O.O..
O#..........#..O#OO....OOO..O#..O..OO.....O....#.....OOOOO.#....O#O..O.....#....#..O....O...#.O#..#.
.O.#.#.O..#.O#O...#.O.O...#..#...#.....#....##O.OOO#...OO..O..................O.#OO...O#.....O...#O.
##..#.#..#.#.O###O#.O..###.......#O..O......#..#.#......O..OO#..#OO...O#...#..OO#O.#.OO#..#..O...O..
........O....O..#..#..O.OOO....O.#O.....#O......O..OO##O#O.#.OO........O.#...OOO..O#...O..O.....#...
..OO.O.O..O...#.......O#.O.O.#O..O..#...#......#.#O#.O....#...#..O......O#...O.##.O....O.O.O.O..O#..
..#..O..#.#O.O...O.#..#..#.##...O.#..#.O..O.#..O....#..OO..OO.#.#...O..OO.......O...#.O#OO..O...#.#O
.#......OO#...##.#.#.....O...#.................O....#....##.O#O.#...O...O#....#O....O....O....###...
...OO.##.OOO...OO..O.O...#......O.....O.......O.O.OO..#O#O.O#....#....#..O##O....#OO#.......O..#...#
O.O..O#O....O.O#O.OO.O.....OOO..O...O.O.##.O.#O.O#.#.#O#......O.#.O..O.#.O....OO##.....#...O.#OOO...
#.#.....#.O.O#.O..O...#OO....O#.......#.#..O..##..#O..O...##.##..O..O#....#...OO...O..OO...#..#..O..
#.O.#.O#..#...O....O..O.O.OO##..........#..O...#.O#OO..O.O.#.........O#.O...O.....#O.O.O...#O...O.##
....#O...O....##.#.O.##O...#..#.#..O.O#..O..#O.#......#.......OO..O.....OOO#O....OO..#O.....O..#..O.
.OO#.....#.OOO....#.....#O###....O.##O...#.##..O.....O......O..O.OOOO.#...O.#..#.###...O..#..O..OO.#
...#O#..O#.O....O.OO.O.#.O..#...........O..#O.....O.....#OO.O#.O....O...#..O..O.#.O..##....##....O.O
###....#..O..#....O.............O#O..........O.O...#.O........#...#.O.....O##...O.#O#...O.O.#O.....O
..O.#.......O.....#..#....O.O.#.O#OO...#.#.#.....#OO.#..#......#...#...#..#.......O#.....O####OO.#.O
.O#....O..O.......#O..#.O#.#..OO.#...#.#.O.O.....O.O.#......#O.#O........O.OO.....OO..O..#OO.....#..
...#.#...O#O.##....O.#....OO..O.OO#...O.OO.OO..O....OO..#..O..O.##.#.OO.#OO..#..O.O.O#.O..OO.O.O#.O.
...#...O.....O...#....O...#...OO#.O#..#....O...........###.O#.....O.##O.O....O...O#....#...#.O...#..
...#..#....#.O.O..#O.#O.........##O....O.#OOO#.O##.#..O....#..#.O....O...OO#O..O.O.#....#.....#O#O#O
..#..#...#.#O......OOO..#.OOO..OO.O#...OO....#O.O.#.#....O...OO#...OO....O..##...#.#O....#.#OO.OO.O.
O.O...#..#O...O##..#..O.#............#..#...##O.O.O....O..O.O...O##.#..O...O..OO..#...O........#....
#.O##..#.....OOO.O..##O...#.O...####.OOO...#...O..#..#......O...#.....#.O.O.O...O##......#...O....#.
...###O.#.O.OO.........O##.#...O..#......O#.#...##O........O.O..O#....O..#.#.O.#.##.O.O#O#....O#.O#O
O...O.O..O.#.......O..O.O....O..O..#..#.........#O.OO..O..O.#O..O.....O.....#O.........#..O.#.#..O..
..O#...#......O..OO...O.#.##O.OO.#...OO..#OO#....#.#.O#..#O.#.OO..O...O#.OO.O...O.#.#.....O..#O....#
....O..#.....#..#.#O.O.OO.#...#.O...#.....##.#..#...OO........O#..O.OO..O.O..O.#...#....O..##..O....
'''

# COMMAND ----------

m = {(row, col): c for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line)}
n_rows = len(inp.splitlines())
n_cols = len(inp.splitlines()[0])
cubes = {pos for pos, c in m.items() if c == '#'}
rollers = {pos for pos, c in m.items() if c == 'O'}

for _ in range(n_rows):
    for row in range(1, n_rows):
        for col in range(n_cols):
            if (row, col) in rollers and (row-1, col) not in cubes.union(rollers):
                rollers.remove((row, col))
                rollers.add((row-1, col))

answer = 0
for roller in rollers:
    answer += n_rows - roller[0]
answer

# COMMAND ----------

import itertools
m = {(row, col): c for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line)}
n_rows = len(inp.splitlines())
n_cols = len(inp.splitlines()[0])
cubes = {pos for pos, c in m.items() if c == '#'}
rollers = {pos for pos, c in m.items() if c == 'O'}

# for _ in range(n_rows):
# for _ in range(100):
for _ in range(1):
    for row, col in sorted(rollers):
        for dr in itertools.count(1):
            if (row-dr, col) not in cubes.union(rollers) and row-dr>=0:
                pass
            else:
                break

        if dr > 1:
            rollers.remove((row, col))
            rollers.add((row-dr+1, col))

answer = 0
for roller in rollers:
    answer += n_rows - roller[0]
answer

# COMMAND ----------

def tilt_north():
    for row, col in sorted(rollers):
        for dr in itertools.count(1):
            if (row-dr, col) not in cubes.union(rollers) and row-dr>=0:
                pass
            else:
                break

        if dr > 1:
            rollers.remove((row, col))
            rollers.add((row-dr+1, col))

def tilt_west():
    for row, col in sorted(rollers, key=lambda x: x[1]):
        for dc in itertools.count(1):
            if (row, col-dc) not in cubes.union(rollers) and col-dc>=0:
                pass
            else:
                break

        if dc > 1:
            rollers.remove((row, col))
            rollers.add((row, col-dc+1))

def tilt_south():
    for row, col in sorted(rollers, reverse=True):
        for dr in itertools.count(1):
            if (row+dr, col) not in cubes.union(rollers) and row+dr<n_rows:
                pass
            else:
                break

        if dr > 1:
            rollers.remove((row, col))
            rollers.add((row+dr-1, col))

def tilt_east():
    for row, col in sorted(rollers, key=lambda x: -x[1]):
        for dc in itertools.count(1):
            if (row, col+dc) not in cubes.union(rollers) and col+dc<n_cols:
                pass
            else:
                break

        if dc > 1:
            rollers.remove((row, col))
            rollers.add((row, col+dc-1))

def cycle():
    tilt_north()
    tilt_west()
    tilt_south()
    tilt_east()

def print_m():
    for row in range(n_rows):
        line = ''
        for col in range(n_cols):
            c = '.'
            if (row, col) in cubes: c = '#'
            if (row, col) in rollers: c = 'O'
            line += c
        print(line)

import itertools
m = {(row, col): c for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line)}
n_rows = len(inp.splitlines())
n_cols = len(inp.splitlines()[0])
cubes = {pos for pos, c in m.items() if c == '#'}
rollers = {pos for pos, c in m.items() if c == 'O'}

# cycle()
# print_m()
# print()
# cycle()
# print_m()
# print()
# cycle()
# print_m()
# print()

nums = []
#for _ in range(200):
for _ in range(121):
    cycle()
    num = sum(n_rows - roller[0] for roller in rollers)
    nums.append(num)
nums

# COMMAND ----------

#example2
cycle_len = 7
prefix = 121
cycle_start = prefix - cycle_len
i = cycle_start + ((1000000000 - prefix) % cycle_len) - 1
nums[i]


# COMMAND ----------

nums = [99836,
99778,
99579,
99533,
99441,
99397,
99380,
99402,
99334,
99344,
99338,
99341,
99365,
99387,
99380,
99397,
99390,
99390,
99388,
99440,
99476,
99545,
99529,
99604,
99645,
99721,
99752,
99779,
99788,
99843,
99891,
99971,
100040,
100078,
100119,
100180,
100216,
100257,
100281,
100301,
100300,
100304,
100324,
100335,
100379,
100407,
100442,
100463,
100481,
100477,
100472,
100462,
100458,
100451,
100449,
100438,
100409,
100390,
100365,
100339,
100304,
100267,
100238,
100215,
100198,
100182,
100169,
100157,
100162,
100160,
100140,
100124,
100109,
100092,
100066,
100042,
100021,
100008,
99997,
99999,
100011,
100025,
100043,
100071,
100084,
100084,
100086,
100084,
100086,
100086,
100079,
100064,
100047,
100034,
100024,
100016,
100008,
100011,
100025,
100043,
100071,
100084,
100084,
100086,
100084,
100086,
100086,
100079,
100064,
100047,
100034,
100024,
100016,
100008,
100011,
100025,
100043,
100071,
100084,
100084,
100086,
]
nums

# COMMAND ----------

#actual
cycle_len = 15
cycle_start = 121 - cycle_len
prefix = 121
i = cycle_start + ((1000000000 - prefix) % cycle_len) - 1
nums[i]
# Not 100011, 100008

# COMMAND ----------

set([100079,
100064,
100047,
100034,
100024,
100016,
100008,
100011,
100025,
100043,
100071,
100084,
100084,
100086]).difference(set([100011, 100008]))

# COMMAND ----------

nums = '''99836
99778
99579
99533
99441
99397
99380
99402
99334
99344
99338
99341
99365
99387
99380
99397
99390
99390
99388
99440
99476
99545
99529
99604
99645
99721
99752
99779
99788
99843
99891
99971
100040
100078
100119
100180
100216
100257
100281
100301
100300
100304
100324
100335
100379
100407
100442
100463
100481
100477
100472
100462
100458
100451
100449
100438
100409
100390
100365
100339
100304
100267
100238
100215
100198
100182
100169
100157
100162
100160
100140
100124
100109
100092
100066
100042
100021
100008
99997
99999
100011
100025
100043
100071
100084
100084
100086
100084
100086
100086
100079
100064
100047
100034
100024
100016
100008
100011
100025
100043
100071
100084
100084
100086
100084
100086
100086
100079
100064
100047
100034
100024
100016
100008
100011
100025
100043
100071
100084
100084
100086
100084
100086
100086
100079
100064
100047
100034
100024
100016
100008
100011
100025
100043
100071
100084
100084
100086
100084
100086
100086
100079
100064
100047
100034
100024
100016
100008
100011
100025
100043
100071
100084
100084
100086
100084
100086
100086
100079
100064
100047
100034
100024
100016
100008
100011
100025
100043
100071
100084
100084
100086
100084
100086
100086
100079
100064
100047
100034
100024
100016
100008
100011
100025
100043
100071
100084
100084
100086
100084
100086
100086
100079
100064
100047
100034
100024
100016
100008
100011
'''
nums = [int(x) for x in nums.splitlines()]
len(nums)
# Cycle 17

# COMMAND ----------

#actual
cycle_len = 17
cycle_start = 200 - cycle_len
prefix = 200
i = cycle_start + ((1000000000 - prefix) % cycle_len) - 1
nums[i]
# Not 100011, 100008

# COMMAND ----------

def tilt_north():
    for col in range(n_cols):
        free = None
        for row in range(n_rows):
            if (row, col) not in cubes and (row, col) not in rollers:
                free = free or row
            if (row, col) in rollers:
                if free:
                    rollers.remove((row,col))
                    rollers.add((free, col))

                    # Find next free spot
                    free = None
                    for r2 in range(free+1, n_rows):
                        if (r2,col) not in cubes and (r2,col) not in rollers:
                            free = r2
                            break

def tilt_west():
    for row, col in sorted(rollers, key=lambda x: x[1]):
        for dc in itertools.count(1):
            if (row, col-dc) not in cubes.union(rollers) and col-dc>=0:
                pass
            else:
                break

        if dc > 1:
            rollers.remove((row, col))
            rollers.add((row, col-dc+1))

def tilt_south():
    for row, col in sorted(rollers, reverse=True):
        for dr in itertools.count(1):
            if (row+dr, col) not in cubes.union(rollers) and row+dr<n_rows:
                pass
            else:
                break

        if dr > 1:
            rollers.remove((row, col))
            rollers.add((row+dr-1, col))

def tilt_east():
    for row, col in sorted(rollers, key=lambda x: -x[1]):
        for dc in itertools.count(1):
            if (row, col+dc) not in cubes.union(rollers) and col+dc<n_cols:
                pass
            else:
                break

        if dc > 1:
            rollers.remove((row, col))
            rollers.add((row, col+dc-1))

def cycle():
    tilt_north()
    tilt_west()
    tilt_south()
    tilt_east()

def print_m():
    for row in range(n_rows):
        line = ''
        for col in range(n_cols):
            c = '.'
            if (row, col) in cubes: c = '#'
            if (row, col) in rollers: c = 'O'
            line += c
        print(line)

import itertools
m = {(row, col): c for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line)}
n_rows = len(inp.splitlines())
n_cols = len(inp.splitlines()[0])
cubes = {pos for pos, c in m.items() if c == '#'}
rollers = {pos for pos, c in m.items() if c == 'O'}

# cycle()
# print_m()
# print()
# cycle()
# print_m()
# print()
# cycle()
# print_m()
# print()

nums = []
for _ in range(200):
    cycle()
    num = sum(n_rows - roller[0] for roller in rollers)
    nums.append(num)
nums

# COMMAND ----------

#example
cycle_start = 193
cycle_len = 7
prefix = 200
i = cycle_start + ((1000000000 - prefix) % cycle_len) - 1
nums[i]

# COMMAND ----------

sorted(rollers, key=lambda x: x[1])

# COMMAND ----------

# for _ in range(100):
#     for row in range(1, n_rows):
#         for col in range(n_cols):
#             if (row, col) in rollers and (row-1, col) not in cubes.union(rollers):
#                 rollers.remove((row, col))
#                 rollers.add((row-1, col))

# answer = 0
# for roller in rollers:
#     answer += n_rows - roller[0]
# answer

# COMMAND ----------

{pos for pos, c in m.items() if c == '#'}

# COMMAND ----------


