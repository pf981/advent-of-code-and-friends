with open("2025_contest/12.txt") as f:
    inp = f.read()

# inp = '''222 267 922 632 944
# 110 33 503 758 129
# 742 697 425 362 568
# 833 408 425 349 631
# 874 671 202 430 602

# SHIFT COL 2 BY 1
# MULTIPLY 4 COL 5
# SUB 28 ALL
# SHIFT COL 4 BY 2
# MULTIPLY 4 ROW 4
# ADD 26 ROW 3
# SHIFT COL 4 BY 2
# ADD 68 ROW 2

# TAKE
# CYCLE
# TAKE
# ACT
# TAKE
# CYCLE'''

grid, instructions, actions = inp.split('\n\n')

g = [[int(num) for num in line.split()] for line in grid.splitlines()]
nrows = len(g)
ncols = len(g[0])

instructions.splitlines()[0].split()

for inst in instructions.splitlines():
    inst = inst.split()

    match inst:
        case ['SHIFT', "COL", col, "BY", by]:
            col = int(col) - 1
            by = int(by)
            values = [g[(r - by) % nrows][col] for r in range(nrows)]
            for r in range(nrows):
                g[r][col] = values[r]
            continue
        case ['SHIFT', "ROW", row, "BY", by]:
            row = int(row) - 1
            by = int(by)
            values = [g[row][(c - by) % ncols] for c in range(ncols)]
            for c in range(ncols):
                g[row][c] = values[c]
            continue
    
    match inst:
        case [_, amount, 'ALL']:
            positions = [(r, c) for r in range(nrows) for c in range(ncols)]
        case [_, amount, 'ROW', row]:
            positions = [(int(row) - 1, c) for c in range(ncols)]
        case [_, amount, 'COL', col]:
            positions = [(r, int(col) - 1) for r in range(nrows)]
        case _:
            assert False
    amount = int(amount)
    # print(f'{amount=}')

    match inst[0]:
        case "ADD":
            f = lambda x: x + amount
        case "SUB":
            f = lambda x: x - amount
        case "MULTIPLY":
            f = lambda x: x * amount
        case _:
            assert False
    for r, c in positions:
        g[r][c] = f(g[r][c]) % 1073741824
# g

answer1 = max(
    max(sum(row) for row in g),
    max(sum(col) for col in zip(*g))
)
# col_sums = [sum(g[r][c] for r in range(nrows)) for c in range(ncols)]
# max(col_sums)

# for r in range(nrows):
#     for c in range(ncols):
#         if not (0 <= g[r][c] <= 1073741823):
#             print(f'Bad {r=} {c=}')



print(answer1)


# Part 2

import collections

g = [[int(num) for num in line.split()] for line in grid.splitlines()]
n = len(g)

q = collections.deque(instructions.splitlines())

for action in actions.splitlines():
    match action:
        case 'TAKE':
            inst = q.popleft()
            continue
        case 'CYCLE':
            q.append(inst)
            continue
        case 'ACT':
            pass
    inst = inst.split()

    match inst:
        case ['SHIFT', "COL", col, "BY", by]:
            col = int(col) - 1
            by = int(by)
            values = [g[(r - by) % n][col] for r in range(n)]
            for r in range(n):
                g[r][col] = values[r]
            continue
        case ['SHIFT', "ROW", row, "BY", by]:
            row = int(row) - 1
            by = int(by)
            values = [g[row][(c - by) % n] for c in range(n)]
            for c in range(n):
                g[row][c] = values[c]
            continue
    
    match inst:
        case [_, amount, 'ALL']:
            positions = [(r, c) for r in range(nrows) for c in range(ncols)]
        case [_, amount, 'ROW', row]:
            positions = [(int(row) - 1, c) for c in range(ncols)]
        case [_, amount, 'COL', col]:
            positions = [(r, int(col) - 1) for r in range(nrows)]
        case _:
            assert False
    amount = int(amount)

    match inst[0]:
        case "ADD":
            f = lambda x: x + amount
        case "SUB":
            f = lambda x: x - amount
        case "MULTIPLY":
            f = lambda x: x * amount
        case _:
            assert False
    for r, c in positions:
        g[r][c] = f(g[r][c]) % 1073741824
# g

answer2 = max(
    max(sum(row) for row in g),
    max(sum(col) for col in zip(*g))
)


print(answer2)


# # Part 3

import itertools
import collections

with open("2025_contest/12.txt") as f:
    inp = f.read()

# inp = '''222 267 922 632 944
# 110 33 503 758 129
# 742 697 425 362 568
# 833 408 425 349 631
# 874 671 202 430 602

# SHIFT COL 2 BY 1
# MULTIPLY 4 COL 5
# SUB 28 ALL
# SHIFT COL 4 BY 2
# MULTIPLY 4 ROW 4
# ADD 26 ROW 3
# SHIFT COL 4 BY 2
# ADD 68 ROW 2

# TAKE
# CYCLE
# TAKE
# ACT
# TAKE
# CYCLE'''
grid, instructions, actions = inp.split('\n\n')

g = [[int(num) for num in line.split()] for line in grid.splitlines()]
n = len(g)

q = collections.deque(instructions.splitlines())
actions_it = itertools.cycle(actions.splitlines())

inst = 'Pending'
while q or inst:
    action = next(actions_it)
    match action:
        case 'TAKE':
            inst = q.popleft()
            continue
        case 'CYCLE':
            q.append(inst)
            inst = None
            continue
        case 'ACT':
            pass
        case _:
            assert False
    inst = inst.split()

    match inst:
        case ['SHIFT', "COL", col, "BY", by]:
            col = int(col) - 1
            by = int(by)
            values = [g[(r - by) % n][col] for r in range(n)]
            for r in range(n):
                g[r][col] = values[r]
            continue
        case ['SHIFT', "ROW", row, "BY", by]:
            row = int(row) - 1
            by = int(by)
            values = [g[row][(c - by) % n] for c in range(n)]
            for c in range(n):
                g[row][c] = values[c]
            continue
    
    match inst:
        case [_, amount, 'ALL']:
            positions = [(r, c) for r in range(n) for c in range(n)]
        case [_, amount, 'ROW', row]:
            positions = [(int(row) - 1, c) for c in range(n)]
        case [_, amount, 'COL', col]:
            positions = [(r, int(col) - 1) for r in range(n)]
        case _:
            assert False
    amount = int(amount)

    match inst[0]:
        case "ADD":
            f = lambda x: x + amount
        case "SUB":
            f = lambda x: x - amount
        case "MULTIPLY":
            f = lambda x: x * amount
        case _:
            assert False
    for r, c in positions:
        g[r][c] = f(g[r][c]) % 1073741824
    inst = None
# g

answer3 = max(
    max(sum(row) for row in g),
    max(sum(col) for col in zip(*g))
)


print(answer3)
# 20927612210 incorrect