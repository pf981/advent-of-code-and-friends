from aocd import get_data

inp = get_data(day=14, year=2023)

from aocd import get_data, submit


def tilt_north(grid):
    for col in range(len(grid[0])):
        free = None
        for row in range(len(grid)):
            if grid[row][col] == '.':
                if free is None:
                    free = row
            elif grid[row][col] == 'O':
                if free is not None:
                    grid[row][col] = '.'
                    grid[free][col] = 'O'

                    # Find next free spot
                    for r2 in range(free + 1, len(grid)):
                        if grid[r2][col] == '.':
                            free = r2
                            break
                    else:
                        free = None
            elif grid[row][col] == '#':
                free = None


inp = get_data(day=14, year=2023)
grid = [list(line) for line in inp.splitlines()]
tilt_north(grid)
answer1 = sum(len(grid) - row for row, line in enumerate(grid) for c in line if c == 'O')
print(answer1)

submit(answer1, part='a', day=14, year=2023)


# Part 2


def rotate_clockwise(grid):
    return [list(z)[::-1] for z in zip(*grid)]


def cycle(grid):
    for _ in range(4):
        tilt_north(grid)
        grid = rotate_clockwise(grid)
    return grid


def to_string(grid):
    return '\n'.join(''.join(line) for line in grid)


grid = [list(line) for line in inp.splitlines()]
seen = {}
loads = []
i = 0
while to_string(grid) not in seen:
    seen[to_string(grid)] = i
    loads.append(sum(len(grid) - row for row, line in enumerate(grid) for c in line if c == 'O'))
    grid = cycle(grid)
    i += 1

cycle_length = i - seen[to_string(grid)]
cycle_start = i - cycle_length
i_answer = cycle_start + ((1000000000 - i) % cycle_length)
answer2 = loads[i_answer]
print(answer2)

submit(answer2, part='b', day=14, year=2023)
