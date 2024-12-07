import collections


with open("./2024/input/everybody_codes_e2024_q15_p1.txt") as f:
    lines = f.read().splitlines()

# lines = '''#####.#####
# #.........#
# #.######.##
# #.........#
# ###.#.#####
# #H.......H#
# ###########'''.splitlines()

nrows = len(lines)
ncols = len(lines[0])

r = 0
c = lines[0].index('.')

q = collections.deque([(r, c)])
d = 0
seen = {(r, c)}
while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        # print(f'{d=} {r=} {c=}')
        if lines[r][c] == 'H':
            break
            
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if r2 < 0 or lines[r2][c2] == '#' or (r2, c2) in seen:
                continue
            seen.add((r2, c2))
            q.append((r2, c2))
    else:
        d += 1
        continue
    break

# print(d)

answer1 = 2 * d
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q15_p2.txt") as f:
    lines = f.read().splitlines()


# lines = '''##########.##########
# #...................#
# #.###.##.###.##.#.#.#
# #..A#.#..~~~....#A#.#
# #.#...#.~~~~~...#.#.#
# #.#.#.#.~~~~~.#.#.#.#
# #...#.#.B~~~B.#.#...#
# #...#....BBB..#....##
# #C............#....C#
# #####################'''.splitlines()

start_r = 0
start_c = lines[0].index('.')

to_collect = tuple(sorted({ch for line in lines for ch in line if ch not in '#.~'}))

# Make sure sort tuple
q = collections.deque([(start_r, start_c, tuple())])
d = 0
seen = {(start_r, start_c)}
while q:
    for _ in range(len(q)):
        r, c, collected = q.popleft()

        # print(f'{d=} {r=} {c=}')
        if collected == to_collect and (r, c) == (0, start_c):
            break
            
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if r2 < 0 or lines[r2][c2] in '#~' or (r2, c2, collected) in seen:
                continue
            
            new_collected = collected
            if lines[r2][c2] != '.' and lines[r2][c2] not in collected:
                new_collected = tuple(sorted(collected + (lines[r2][c2],)))

            seen.add((r2, c2, new_collected))
            q.append((r2, c2, new_collected))
    else:
        d += 1
        continue
    break

answer2 = d
print(answer2)



# Part 3


with open("./2024/input/everybody_codes_e2024_q15_p3.txt") as f:
    lines = f.read().splitlines()


start_r = 0
start_c = lines[0].index('.')

to_collect = tuple(sorted({ch for line in lines for ch in line if ch not in '#.~'}))

# Make sure sort tuple
q = collections.deque([(start_r, start_c, tuple())])
d = 0
seen = {(start_r, start_c)}
shortest = {} # 
while q:
    for _ in range(len(q)):
        r, c, collected = q.popleft()

        # print(f'{d=} {r=} {c=}')
        if collected == to_collect and (r, c) == (0, start_c):
            break
            
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if r2 < 0 or lines[r2][c2] in '#~' or (r2, c2, collected) in seen:
                continue
            
            new_collected = collected
            if lines[r2][c2] != '.' and lines[r2][c2] not in collected:
                new_collected = tuple(sorted(collected + (lines[r2][c2],)))

            seen.add((r2, c2, new_collected))
            q.append((r2, c2, new_collected))
    else:
        d += 1
        continue
    break

answer3 = d
print(answer3)

