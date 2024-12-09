from aocd import get_data

inp = get_data(day=10, year=2023)

from aocd import get_data, submit
import collections


inp = get_data(day=10, year=2023)
m = collections.defaultdict(lambda: '.', {(row, col): c for row, line in enumerate(inp.splitlines()) for col, c in enumerate(line)})
start_pos = next(pos for pos, c in m.items() if c == 'S')
m[start_pos] = 'F' # Hard coded based on input
q = collections.deque([(start_pos, 0)])
distances = {}

while q:
    pos, d = q.popleft()
    if pos in distances:
        continue
    distances[pos] = d

    d += 1
    if m[pos] in '|LJ': # N
        q.append(((pos[0] - 1, pos[1]), d))
    if m[pos] in '-LF': # E
        q.append(((pos[0], pos[1] + 1), d))
    if m[pos] in '|7F': # S
        q.append(((pos[0] + 1, pos[1]), d))
    if m[pos] in '-J7': # W
        q.append(((pos[0], pos[1] - 1), d))

answer1 = max(distances.values())
print(answer1)

submit(answer1, part='a', day=10, year=2023)


# Part 2


import re


# Traverse the loop clockwise and mark everything on the right as "external". Right being external is hard-coded based on the specific input.
external = set()
pos = list(start_pos)
direction = 'N'
while True:
    pos2 = tuple(pos)
    if direction == 'E': # Heading east
        if m[pos2] == '-':
            external.add((pos[0] + 1, pos[1])) # S
            pos[1] += 1 # E
        elif m[pos2] == 'J':
            external.add((pos[0] + 1, pos[1])) # S, E, SE
            external.add((pos[0], pos[1] + 1))
            external.add((pos[0] + 1, pos[1] + 1))
            pos[0] -= 1 # N
            direction = 'N'
        elif m[pos2] == '7':
            external.add((pos[0] + 1, pos[1] - 1)) # SW
            pos[0] += 1 # S
            direction = 'S'
    elif direction == 'S': # Heading south
        if m[pos2] == '|':
            external.add((pos[0], pos[1] - 1)) # W
            pos[0] += 1 # S
        elif m[pos2] == 'L':
            external.add((pos[0], pos[1] - 1)) # W, SW, S
            external.add((pos[0] + 1, pos[1] - 1))
            external.add((pos[0] + 1, pos[1]))
            pos[1] += 1 # E
            direction = 'E'
        elif m[pos2] == 'J':
            external.add((pos[0] - 1, pos[1] - 1)) # NW
            pos[1] -= 1 # W
            direction = 'W'
    if direction == 'W': # Heading west
        if m[pos2] == '-':
            external.add((pos[0] - 1, pos[1])) # N
            pos[1] -= 1 # W
        elif m[pos2] == 'L':
            external.add((pos[0] - 1, pos[1] + 1)) # NE
            pos[0] -= 1# N
            direction = 'N'
        elif m[pos2] == 'F':
            external.add((pos[0] - 1, pos[1])) # N, W, NW
            external.add((pos[0], pos[1] - 1))
            external.add((pos[0] - 1, pos[1] - 1))
            pos[0] += 1 # S
            direction = 'S'
    elif direction == 'N': # Heading north
        if m[pos2] == '|':
            external.add((pos[0], pos[1] + 1)) # E
            pos[0] -= 1 # N
        elif m[pos2] == '7':
            external.add((pos[0], pos[1] + 1)) # E, N, NE
            external.add((pos[0] - 1, pos[1]))
            external.add((pos[0] - 1, pos[1] + 1))
            pos[1] -= 1 # W
            direction = 'W'
        elif m[pos2] == 'F':
            external.add((pos[0] + 1, pos[1] + 1)) # SE
            pos[1] += 1 # E
            direction = 'E'

    if tuple(pos) == start_pos:
        break

graphic = ''
n_rows = max(row for row, _ in m)
n_cols = max(col for _, col in m)
for row in range(n_rows):
    for col in range(n_cols):
        c = '.' if (row, col) not in distances else m[(row, col)]
        if c == '.' and (row, col) in external:
            c = 'O'
        graphic += c
    graphic += '\n'

# Do some basic replacements to determine what is internal
# Any . next to a pipe MUST be internal - otherwise it would be an O
graphic = re.sub(r'([|LJ7F-])\.', r'\1#', graphic)
for _ in range(100):
    graphic = graphic.replace('#.', '##')
print(graphic)

answer2 = graphic.count('#')
print(answer2)

submit(answer2, part='b', day=10, year=2023)
