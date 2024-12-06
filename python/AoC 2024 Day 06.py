from aocd import get_data, submit


inp = get_data(day=6, year=2024)

# inp = '''....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# '''

lines = inp.splitlines()
nrows = len(lines)
ncols = len(lines[0])

start = 0, 0
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c == '^':
            start = row, col
            break
    else:
        continue
    break
seen = set()
r, c  = start
direction = 'N'
rot = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N',
}

while 0 <= r < nrows and 0 <= c < ncols:
    seen.add((r, c))
    
    r2 = r + (direction == 'S') - (direction == 'N')
    c2 = c + (direction == 'E') - (direction == 'W')
    if not (0 <= r2 < nrows) or not ( 0 <= c2 < ncols):
        break
    i = 0
    while lines[r2][c2] == '#':
        if i == 10:
            break
        i += 1
        # print(f'{r2=} {c2=}')
        direction = rot[direction]
        r2 = r + (direction == 'S') - (direction == 'N')
        c2 = c + (direction == 'E') - (direction == 'W')
    r = r2
    c = c2

answer1 = len(seen)
print(answer1)

# submit(answer1, part='a', day=6, year=2024)


# Part 2

inp = get_data(day=6, year=2024)

# inp = '''....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# '''

lines = inp.splitlines()
lines = [list(line) for line in lines]
nrows = len(lines)
ncols = len(lines[0])

import copy

start = 0, 0
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c == '^':
            start = row, col
            break
    else:
        continue
    break
seen = set()
r, c  = start
direction = 'N'
rot = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N',
}


def is_good(lines):
    direction = 'N'
    r, c  = start

    states = set() # r, c, direction
    while 0 <= r < nrows and 0 <= c < ncols:
        if (r, c, direction) in  states:
            return True
        states.add((r,c,direction))
        seen.add((r, c))
        
        r2 = r + (direction == 'S') - (direction == 'N')
        c2 = c + (direction == 'E') - (direction == 'W')
        if not (0 <= r2 < nrows) or not ( 0 <= c2 < ncols):
            return False
        while lines[r2][c2] == '#':
            direction = rot[direction]
            r2 = r + (direction == 'S') - (direction == 'N')
            c2 = c + (direction == 'E') - (direction == 'W')
        r = r2
        c = c2
    return False

answer2 = 0
for r in range(nrows):
    for c in range(ncols):
        if lines[r][c] != '.':
            continue
        lines[r][c] = '#'
        if is_good(lines):
            answer2 += 1
        lines[r][c] = '.'

print(answer2)

submit(answer2, part='b', day=6, year=2024)
