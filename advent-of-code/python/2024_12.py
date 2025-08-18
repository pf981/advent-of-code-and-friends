from aocd import get_data, submit


inp = get_data(day=12, year=2024)
lines = inp.splitlines()
nrows = len(lines)
ncols = len(lines[0])


def is_valid(r, c):
    return (0 <= r < nrows) and (0 <= c < ncols)


def has_wall(r, c, direction):
    r2 = r + (direction == 'S') - (direction == 'N')
    c2 = c + (direction == 'E') - (direction == 'W')
    return not is_valid(r2, c2) or lines[r][c] != lines[r2][c2]


def get_area_perim(r, c, is_part2):
    if (r, c) in seen:
        return 0, 0
    seen.add((r, c))

    perim = 4
    area = 1
    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc
        if not is_valid(r2, c2) or lines[r2][c2] != lines[r][c]:
            continue
        perim -= 1
        if (r2, c2) in seen:
            continue
        area2, perim2 = get_area_perim(r2, c2, is_part2)
        area += area2
        perim += perim2
    
    if is_part2:
        for wall_direction in 'EW':
            if has_wall(r, c, wall_direction) and is_valid(r - 1, c) and lines[r][c] == lines[r - 1][c] and has_wall(r - 1, c, wall_direction):
                perim -= 1
        for wall_direction in 'NS':
            if has_wall(r, c, wall_direction) and is_valid(r, c + 1) and lines[r][c] == lines[r][c + 1] and has_wall(r, c + 1, wall_direction):
                perim -= 1

    return area, perim


seen = set()
answer1 = 0
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if (r, c) in seen:
            continue
        area, perim = get_area_perim(r, c, False)
        answer1 += area * perim
print(answer1)

submit(answer1, part='a', day=12, year=2024)


# Part 2


seen = set()
answer2 = 0
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if (r, c) in seen:
            continue
        area, perim = get_area_perim(r, c, True)
        answer2 += area * perim
print(answer2)

submit(answer2, part='b', day=12, year=2024)
