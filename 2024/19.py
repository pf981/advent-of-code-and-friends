import itertools

with open("./2024/input/everybody_codes_e2024_q19_p1.txt") as f:
    lines = f.read().splitlines()


def rot_r(g, r, c):
    g[r-1][c-1],g[r-1][c],g[r-1][c+1],g[r][c+1],g[r+1][c+1],g[r+1][c],g[r+1][c-1],g[r][c-1] =\
        g[r][c-1],g[r-1][c-1],g[r-1][c],g[r-1][c+1],g[r][c+1],g[r+1][c+1],g[r+1][c],g[r+1][c-1]

def rot_l(g, r, c):
    g[r-1][c-1],g[r-1][c],g[r-1][c+1],g[r][c+1],g[r+1][c+1],g[r+1][c],g[r+1][c-1],g[r][c-1] =\
        g[r-1][c],g[r-1][c+1],g[r][c+1],g[r+1][c+1],g[r+1][c],g[r+1][c-1],g[r][c-1],g[r-1][c-1]

# lines = '''LR

# >-IN-
# -----
# W---<'''.splitlines()

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

# lines = '''RRLL

# A.VI..>...T
# .CC...<...O
# .....EIB.R.
# .DHB...YF..
# .....F..G..
# D.H........'''.splitlines()

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
    

for line in grid:
    print(''.join(line))

import collections
counts = collections.Counter()
for line in grid:
    for c in line:
        counts[c] += 1
print(counts)


# TODOD: Get nums between ">xxx<"
# answer2 = int(''.join(grid[1][1:-1]))
# print(answer2)


# Part 3

1_048_576_000 



with open("./2024/input/everybody_codes_e2024_q19_p3.txt") as f:
    lines = f.read().splitlines()

lines = '''RRLL

A.VI..>...T
.CC...<...O
.....EIB.R.
.DHB...YF..
.....F..G..
D.H........'''.splitlines()

ops, _, *grid = lines
grid = [list(line) for line in grid]

nrows = len(grid)
ncols = len(grid[0])

# seen = {tuple(tuple(line) for line in grid): 0}
# for i in itertools.count():
#     op_it = itertools.cycle(ops)
#     for r in range(1, nrows - 1):
#         for c in range(1, ncols - 1):
#             if next(op_it) == 'R':
#                 rot_r(grid, r, c)
#             else:
#                 rot_l(grid, r, c)
#     tup = tuple(tuple(line) for line in grid)
#     if tup in seen:
#         break
#     seen[tup] = i

# answer3 = 'todo'
# print(answer3)


# import collections
# counts = collections.Counter()
# for line in grid:
#     for c in line:
#         counts[c] += 1
# print(counts)


# Okay, so basically simulate only the points with numbers 1-9. 0s don't count.
# Lookup rot
# In a single iteration, pi -> pj. That is the same every iteration for every position

m = {}  # (r, c) -> (r2, c2). Position after full iteration
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
        m[(r, c)] = pos_grid[r][c]



def map_pos(r, c, n_iterations):
    seen = {} # (r, c) -> i
    for i in itertools.count():
        (r, c) = m[(r, c)]
        if (r, c) in seen:
            cycle_length = i - seen[(r, c)]
            print(f'{cycle_length=} {i=} {r=} {c=} {seen[(r, c)]=}')
            break
        seen[(r, c)] = i
    # print(i, cycle_length)

    n_cycles = (n_iterations - i) // cycle_length
    remaining = n_iterations - (n_cycles * cycle_length)
    for _ in range(remaining):
        (r, c) = m[(r, c)]
    return r, c

# Test
r, c = 0, 0
map_pos(0, 0, 100)

result = {}
for r, line in enumerate(grid):
    for c, ch in enumerate(line):
        if ch in '123456789<>':
            r2, c2 = map_pos(r, c, 100)
            result[(r2, c2)] = ch

r, c = next((r, c) for r, line in enumerate(grid) for c, ch in enumerate(line) if ch == '>')
map_pos(r, c, 100)

map_pos(r, c, n_iterations)

r, c = next((r, c) for r, line in enumerate(grid) for c, ch in enumerate(line) if ch == '>')
print(r, c)
for _ in range(100):
    (r, c) = m[(r, c)]
print(r, c)



##########################################



import itertools

def rot_r(g, r, c):
    g[r-1][c-1],g[r-1][c],g[r-1][c+1],g[r][c+1],g[r+1][c+1],g[r+1][c],g[r+1][c-1],g[r][c-1] =\
        g[r][c-1],g[r-1][c-1],g[r-1][c],g[r-1][c+1],g[r][c+1],g[r+1][c+1],g[r+1][c],g[r+1][c-1]

def rot_l(g, r, c):
    g[r-1][c-1],g[r-1][c],g[r-1][c+1],g[r][c+1],g[r+1][c+1],g[r+1][c],g[r+1][c-1],g[r][c-1] =\
        g[r-1][c],g[r-1][c+1],g[r][c+1],g[r+1][c+1],g[r+1][c],g[r+1][c-1],g[r][c-1],g[r-1][c-1]

# with open("./2024/input/everybody_codes_e2024_q19_p2.txt") as f:
#     lines = f.read().splitlines()


with open("./2024/input/everybody_codes_e2024_q19_p3.txt") as f:
    lines = f.read().splitlines()

# lines = '''RRLL

# A.VI..>...T
# .CC...<...O
# .....EIB.R.
# .DHB...YF..
# .....F..G..
# D.H........'''.splitlines()

ops, _, *grid = lines
grid = [list(line) for line in grid]

nrows = len(grid)
ncols = len(grid[0])

# for _ in range(100):
#     op_it = itertools.cycle(ops)
#     for r in range(1, nrows - 1):
#         for c in range(1, ncols - 1):
#             if next(op_it) == 'R':
#                 rot_r(grid, r, c)
#             else:
#                 rot_l(grid, r, c)

# for line in grid:
#     print(''.join(line))



m = {}  # (r, c) -> (r2, c2). Position after full iteration
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
        m[pos_grid[r][c]] = (r, c)
        # m[(r, c)] = pos_grid[r][c]



# result = [['XXXXX' for c in range(ncols)] for r in range(nrows)]
# for r in range(nrows):
#     for c in range(ncols):
#         ch = grid[r][c]
#         r2, c2 = r, c
#         for _ in range(100):
#             # print(f'{(r2,c2)=} {m[(r2,c2)]=}')
#             r2, c2 = m[(r2, c2)]
#         result[r2][c2] = ch
# for line in result:
#     print(''.join(line))



# # TEST
# # r, c = next((r, c) for r, line in enumerate(grid) for c, ch in enumerate(line) if ch == '>')
# r, c = next((r, c) for r, line in enumerate(grid) for c, ch in enumerate(line) if ch == '1')
# print(r, c)
# for _ in range(100):
#     print(r, c)
#     (r, c) = m[(r, c)]
# print(r, c)

# for _ in range(100):
#     op_it = itertools.cycle(ops)
#     for r in range(1, nrows - 1):
#         for c in range(1, ncols - 1):
#             if next(op_it) == 'R':
#                 rot_r(grid, r, c)
#             else:
#                 rot_l(grid, r, c)





def map_pos(r, c, n_iterations):
    n_iterations -= 1
    seen = {} # (r, c) -> i
    for i in itertools.count():
        (r, c) = m[(r, c)]
        if (r, c) in seen:
            cycle_length = i - seen[(r, c)]
            # print(f'{cycle_length=} {i=} {r=} {c=} {seen[(r, c)]=}')
            break
        seen[(r, c)] = i
    # print(i, cycle_length)

    n_cycles = (n_iterations - i) // cycle_length
    remaining = n_iterations - (n_cycles * cycle_length)
    for _ in range(remaining):
        (r, c) = m[(r, c)]
    return r, c



result = [['.' for c in range(ncols)] for r in range(nrows)]
for r in range(nrows):
    for c in range(ncols):
        ch = grid[r][c]
        if ch not in '1234567890<>':
            continue
        r2, c2 = map_pos(r, c, 1048576000)
        result[r2][c2] = ch
for line in result:
    print(''.join(line))


# result = [['XXXXX' for c in range(ncols)] for r in range(nrows)]
# for r in range(nrows):
#     for c in range(ncols):
#         ch = grid[r][c]
#         r2, c2 = map_pos(r, c, 99)
#         result[r2][c2] = ch
# for line in result:
#     print(''.join(line))