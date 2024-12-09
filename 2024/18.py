import collections


with open("./2024/input/everybody_codes_e2024_q18_p1.txt") as f:
    lines = f.read().splitlines()

# lines = '''##########
# ..#......#
# #.P.####P#
# #.#...P#.#
# ##########'''.splitlines()

nrows = len(lines)
ncols = len(lines[0])

q = collections.deque([(1, 0)])
d = 0
remaining_p = sum(c == 'P' for line in lines for c in line)
seen = set((1, 0))
while remaining_p:
    for _ in range(len(q)):
        r, c = q.popleft()

        if lines[r][c] == 'P':
            remaining_p -= 1
        
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if c2 < 0 or (r2, c2) in seen or lines[r2][c2] == '#':
                continue
            seen.add((r2, c2))
            q.append((r2, c2))
    d += 1

answer1 = d - 1
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q18_p2.txt") as f:
    lines = f.read().splitlines()


# lines = '''#######################
# ...P..P...#P....#.....#
# #.#######.#.#.#.#####.#
# #.....#...#P#.#..P....#
# #.#####.#####.#########
# #...P....P.P.P.....P#.#
# #.#######.#####.#.#.#.#
# #...#.....#P...P#.#....
# #######################'''.splitlines()

nrows = len(lines)
ncols = len(lines[0])

q = collections.deque([(1, 0), (nrows - 2, ncols - 1)])
d = 0
remaining_p = sum(c == 'P' for line in lines for c in line)
seen = {(1, 0), (nrows - 2, ncols - 1)}
while remaining_p:
    for _ in range(len(q)):
        r, c = q.popleft()

        if lines[r][c] == 'P':
            remaining_p -= 1
        
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if not (0 <= c2 < ncols) or (r2, c2) in seen or lines[r2][c2] == '#':
                continue
            seen.add((r2, c2))
            q.append((r2, c2))
    d += 1

answer2 = d - 1
print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q18_p3.txt") as f:
    lines = f.read().splitlines()

# lines = '''##########
# #.#......#
# #.P.####P#
# #.#...P#.#
# ##########'''.splitlines()

nrows = len(lines)
ncols = len(lines[0])

q = collections.deque() # [(r, c, p_index), ...]
seen = {}
p_index = 0
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == 'P':
            q.append((r, c, p_index))
            seen[(r, c)] = {p_index: 0}
            p_index += 1
        elif ch == '.':
            seen[(r, c)] = {}
n_ps = p_index

d = 0
answer3 = float('inf')
while q:
    for _ in range(len(q)):
        r, c, p_index = q.popleft()

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if lines[r2][c2] == '#':
                continue

            if p_index in seen[(r2, c2)]:
                continue
            seen[(r2, c2)][p_index] = d
            if len(seen[(r2, c2)]) == n_ps and lines[r2][c2] == '.':
                # print(f'{r2=} {c2=} {seen[(r2, c2)]=} s={sum(seen[(r2, c2)].values())}')
                answer3 = min(answer3, sum(dd + 1 for dd in seen[(r2, c2)].values()))
                # answer3 = min(answer3, sum(seen[(r2, c2)].values()))
            q.append((r2, c2, p_index))
    d += 1

print(answer3)
