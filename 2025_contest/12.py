import collections
import itertools


def perform_instuction(g: list[list[int]], inst: str) -> None:
    inst = inst.split()
    n = len(g)

    match inst:
        case ['SHIFT', "COL", col, "BY", by]:
            col = int(col) - 1
            values = [g[(r - int(by)) % n][col] for r in range(n)]
            for r in range(n):
                g[r][col] = values[r]
            return
        case ['SHIFT', "ROW", row, "BY", by]:
            row = int(row) - 1
            values = [g[row][(c - int(by)) % n] for c in range(n)]
            for c in range(n):
                g[row][c] = values[c]
            return

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
    f = {"ADD": lambda x: x + amount, "SUB": lambda x: x - amount, "MULTIPLY": lambda x: x * amount}[inst[0]]

    for r, c in positions:
        g[r][c] = f(g[r][c]) % 1073741824


with open("2025_contest/12.txt") as f:
    inp = f.read()


grid, instructions, actions = inp.split('\n\n')

g = [[int(num) for num in line.split()] for line in grid.splitlines()]
for inst in instructions.splitlines():
    perform_instuction(g, inst)

answer1 = max(
    max(sum(row) for row in g),
    max(sum(col) for col in zip(*g))
)
print(answer1)


# Part 2

g = [[int(num) for num in line.split()] for line in grid.splitlines()]
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
            perform_instuction(g, inst)

answer2 = max(
    max(sum(row) for row in g),
    max(sum(col) for col in zip(*g))
)
print(answer2)


# Part 3

g = [[int(num) for num in line.split()] for line in grid.splitlines()]
q = collections.deque(instructions.splitlines())
actions_it = itertools.cycle(actions.splitlines())

while True:
    action = next(actions_it)
    match action:
        case 'TAKE':
            if not q:
                break
            inst = q.popleft()
            continue
        case 'CYCLE':
            q.append(inst)
            inst = None
            continue
        case 'ACT':
            perform_instuction(g, inst)

answer3 = max(
    max(sum(row) for row in g),
    max(sum(col) for col in zip(*g))
)
print(answer3)
