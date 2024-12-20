from aocd import get_data, submit
import collections

inp = get_data(day=20, year=2024)

# inp = '''###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############
# '''

lines = inp.splitlines()

nrows = len(lines)
ncols = len(lines[0])

start = end = None
for row, line in enumerate(lines):
    for col, ch in enumerate(line):
        if ch == 'S':
            start = (row, col)
        elif ch == 'E':
            end = (row, col)

q = collections.deque([(start[0], start[1], None)]) # (r, c), cheat_pos
d = 0
finish_times = []
legit_time = None
seen = {(start[0], start[1], None)}
while q and not legit_time:
    for _ in range(len(q)):
        r, c, cheat_pos = q.popleft()

        if (r, c) == end:
            # print(f'END! {r, c=}')
            if not cheat_pos:
                legit_time = d
                break
            finish_times.append((d, cheat_pos))
            continue
        
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            cheat_pos2 = cheat_pos
            if not (0 <= r2 < nrows) or not (0 <= c2 < ncols):
                continue

            if lines[r2][c2] == '#':
                if cheat_pos:
                    continue
                cheat_pos2 = (r2, c2)
            if (r2, c2, cheat_pos2) in seen:
                continue
            seen.add((r2, c2, cheat_pos2))
            q.append((r2, c2, cheat_pos2))

    d += 1



def get_saves(delta):
    result = set()
    for t, pos in finish_times:
        if legit_time - t >= delta:
            result.add(pos)
    return len(result)

# get_saves(64)
# get_saves(40)

# get_saves(2)
# get_saves(4)
# get_saves(6)
# get_saves(14)

answer1 = get_saves(100)
print(answer1)

# submit(answer1, part='a', day=20, year=2024)


# Part 2


# answer2 = 'todo'
# print(answer2)

# submit(answer2, part='b', day=20, year=2024)






from aocd import get_data, submit
import collections

inp = get_data(day=20, year=2024)

# inp = '''###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############
# '''

lines = inp.splitlines()

nrows = len(lines)
ncols = len(lines[0])

start = end = None
dots = 0
for row, line in enumerate(lines):
    for col, ch in enumerate(line):
        if ch == 'S':
            start = (row, col)
        elif ch == 'E':
            end = (row, col)
        if ch != '#':
            dots += 1

q = collections.deque([start]) # (r, c)
d = 1
time_from_start = {start: 0} # (r, c) -> t
while end not in time_from_start:
    for _ in range(len(q)):
        r, c = q.popleft()

        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if lines[r2][c2] == '#':
                continue
            if (r2, c2) in time_from_start:
                continue
            time_from_start[(r2, c2)] = d
            q.append((r2, c2))
    d += 1

legit_time = time_from_start[end]

# len(time_from_start)
# dots

# Check if goes through end

def get_saves(min_savings, duration):
    result = 0
    for (r,c), t in time_from_start.items():
        for (r2, c2), t2 in time_from_start.items():
            if (r, c) == (r2, c2):
                continue
            d = abs(r - r2) + abs(c - c2)
            if d <= duration: # TODO: <=?
                # print(f'{r, c=} {t=} {r2, c2=} {t2=}')
                result += t2 - t - d >= min_savings # TODO: <=?
    return result

answer1 = get_saves(100, 2)
print(answer1)
answer2 = get_saves(100, 20)
print(answer2)

submit(answer2, part='b', day=20, year=2024)