import itertools


def rot_r(g: list[list[str]], r: int, c: int) -> None:
    g[r-1][c-1],g[r-1][c],g[r-1][c+1],g[r][c+1],g[r+1][c+1],g[r+1][c],g[r+1][c-1],g[r][c-1] = (
        g[r][c-1],g[r-1][c-1],g[r-1][c],g[r-1][c+1],g[r][c+1],g[r+1][c+1],g[r+1][c],g[r+1][c-1]
    )

def rot_l(g: list[list[str]], r: int, c: int) -> None:
    g[r-1][c-1],g[r-1][c],g[r-1][c+1],g[r][c+1],g[r+1][c+1],g[r+1][c],g[r+1][c-1],g[r][c-1] = (
        g[r-1][c],g[r-1][c+1],g[r][c+1],g[r+1][c+1],g[r+1][c],g[r+1][c-1],g[r][c-1],g[r-1][c-1]
    )


with open("./2024/input/everybody_codes_e2024_q19_p1.txt") as f:
    lines = f.read().splitlines()

ops, _, *grid = lines
grid = [list(line) for line in grid]
nrows = len(grid)
ncols = len(grid[0])

op_it = itertools.cycle(ops)
for r in range(1, nrows - 1):
    for c in range(1, ncols - 1):
        if next(op_it) == 'R':
            rot_r(grid, r, c)
        else:
            rot_l(grid, r, c)
    

answer1 = int(''.join(grid[1][1:-1]))
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q19_p2.txt") as f:
    lines = f.read().splitlines()

ops, _, *grid = lines
grid = [list(line) for line in grid]
nrows = len(grid)
ncols = len(grid[0])

for _ in range(100):
    op_it = itertools.cycle(ops)
    for r in range(1, nrows - 1):
        for c in range(1, ncols - 1):
            if next(op_it) == 'R':
                rot_r(grid, r, c)
            else:
                rot_l(grid, r, c)

answer2 = None
for line in grid:
    if '>' in line:
        answer2 = int(''.join(line[line.index('>') + 1:line.index('<')]))
        break
print(answer2)


# Part 3


def map_pos(r: int, c: int, n_iterations: int, position_map: dict[tuple[int, int], tuple[int, int]]) -> tuple[int, int]:
    n_iterations -= 1
    seen = {} # (r, c) -> i
    for i in itertools.count():
        (r, c) = position_map[(r, c)]
        if (r, c) in seen:
            cycle_length = i - seen[(r, c)]
            break
        seen[(r, c)] = i

    n_cycles = (n_iterations - i) // cycle_length
    remaining = n_iterations - (n_cycles * cycle_length)
    for _ in range(remaining):
        (r, c) = position_map[(r, c)]

    return r, c


with open("./2024/input/everybody_codes_e2024_q19_p3.txt") as f:
    lines = f.read().splitlines()

ops, _, *grid = lines
grid = [list(line) for line in grid]
nrows = len(grid)
ncols = len(grid[0])

position_map = {}  # (r, c) -> (r2, c2). Position after full iteration
pos_grid = [[(r, c) for c in range(ncols)] for r in range(nrows)]
op_it = itertools.cycle(ops)
for r in range(1, nrows - 1):
    for c in range(1, ncols - 1):
        if next(op_it) == 'R':
            rot_r(pos_grid, r, c)
        else:
            rot_l(pos_grid, r, c)
for r in range(nrows):
    for c in range(ncols):
        position_map[pos_grid[r][c]] = (r, c)

final_grid = [['.' for c in range(ncols)] for r in range(nrows)]
for r in range(nrows):
    for c in range(ncols):
        ch = grid[r][c]
        if ch not in '1234567890<>':
            continue
        r2, c2 = map_pos(r, c, 1048576000, position_map)
        final_grid[r2][c2] = ch

answer3 = None
for line in final_grid:
    if '>' in line:
        answer3 = int(''.join(line[line.index('>') + 1:line.index('<')]))
        break
print(answer3)
