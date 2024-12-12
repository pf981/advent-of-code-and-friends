from aocd import get_data, submit


inp = get_data(day=12, year=2024)

# inp = '''AAAA
# BBCD
# BBCC
# EEEC
# '''

lines = inp.splitlines()
nrows = len(lines)
ncols = len(lines[0])

seen = set()

def get_area_perim(r, c):
    if (r, c) in seen:
        return 0, 0
    seen.add((r, c))

    perim = 4
    area = 1
    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc
        if not (0 <= r2 < nrows) or not (0 <= c2 < ncols):
            continue
        if lines[r2][c2] != lines[r][c]:
            continue
        perim -= 1
        if (r2, c2) in seen:
            continue
        a2, p2 = get_area_perim(r2, c2)
        perim += p2
        area += a2

    return area, perim

answer1 = 0
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if (r, c) in seen:
            continue
        area, perim = get_area_perim(r, c)
        print(f'{r=} {c=} {ch=} {area=} {perim=}')
        answer1 += area * perim

print(answer1)

submit(answer1, part='a', day=12, year=2024)


# Part 2

from aocd import get_data, submit

inp = get_data(day=12, year=2024)

inp = '''AAAA
BBCD
BBCC
EEEC
'''

lines = inp.splitlines()
nrows = len(lines)
ncols = len(lines[0])

seen = set()

def is_valid(r, c):
    return (0 <= r < nrows) and (0 <= c < ncols)

def has_n_wall(r, c):
    if not is_valid(r-1, c) or lines[r][c] != lines[r-1][c]:
        return True
def has_e_wall(r, c):
    if not is_valid(r, c+1) or lines[r][c] != lines[r][c+1]:
        return True
def has_s_wall(r, c):
    if not is_valid(r+1, c) or lines[r][c] != lines[r+1][c]:
        return True
def has_w_wall(r, c):
    if not is_valid(r, c-1) or lines[r][c] != lines[r][c-1]:
        return True

def get_area_perim(r, c):
    if (r, c) in seen:
        return 0, 0
    seen.add((r, c))

    perim = 4
    area = 1
    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc
        if not (0 <= r2 < nrows) or not (0 <= c2 < ncols):
            continue
        if lines[r2][c2] != lines[r][c]:
            continue
        perim -= 1
        if (r2, c2) in seen:
            continue
        a2, p2 = get_area_perim(r2, c2)
        perim += p2
        area += a2
    
    # print(r, c)
    # E wall; N check
    # Return false if invalid
    if has_e_wall(r, c) and is_valid(r-1, c) and lines[r][c] == lines[r-1][c] and has_e_wall(r-1, c):
        perim -= 1

    # N wall; east check
    if has_n_wall(r, c) and is_valid(r, c+1) and lines[r][c] == lines[r][c+1] and has_n_wall(r, c+1):
        perim -= 1

    # S wall; E check
    if has_s_wall(r, c) and is_valid(r, c+1) and lines[r][c] == lines[r][c+1] and has_s_wall(r, c+1):
        perim -= 1

    # W wall; N check
    if has_w_wall(r, c) and is_valid(r-1, c) and lines[r][c] == lines[r-1][c] and has_w_wall(r-1, c):
        perim -= 1

    return area, perim

answer2 = 0
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if (r, c) in seen:
            continue
        area, perim = get_area_perim(r, c)
        print(f'{r=} {c=} {ch=} {area=} {perim=}')
        answer2 += area * perim

print(answer2)

submit(answer2, part='b', day=12, year=2024)
