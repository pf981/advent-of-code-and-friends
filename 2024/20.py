# import collections
# import heapq


# with open("./2024/input/everybody_codes_e2024_q20_p1.txt") as f:
#     lines = f.read().splitlines()

# # lines = '''#....S....#
# # #.........#
# # #---------#
# # #.........#
# # #..+.+.+..#
# # #.+-.+.++.#
# # #.........#'''.splitlines()

# nrows = len(lines)
# ncols = len(lines[0])
# start_r, start_c = next((r, c) for r, line in enumerate(lines) for c, ch in enumerate(line) if ch == 'S')

# delta = {
#     'S': -1,
#     '.': -1,
#     '+': +1,
#     '-': -2
# }

# targets = {
#     # (5, 8),
#     (5, 7),
#     # (4, 7),
# }
# per_cycle = 2

# def find_best():
#     heap = [(-(1000 + 100 // 4 * per_cycle), 100, 1000, start_r, start_c)] # neg_potential, t, altitude, r, c
#     heapq.heapify(heap)

#     seen = {(start_r, start_c)}
#     while heap:
#         neg_potential, t, altitude, r, c = heapq.heappop(heap)

#         if (r, c) in targets:
#             print(f'{r,c=} {altitude=}')
#             print(f'{t/4=}')
#             return -neg_potential + [1,1,2][t%4] # Specific to example

#         for direction in 'NESW':
#             r2 = r + (direction == 'S') - (direction == 'N')
#             c2 = c + (direction == 'E') - (direction == 'W')
#             if not (0 <= r2 < nrows) or not (0 <= c2 < ncols) or lines[r2][c2] == '#' or (r2, c2) in seen:
#                 continue
#             seen.add((r2, c2))
#             altitude2 = altitude + delta[lines[r2][c2]]
#             t2 = t - 1
#             neg_potential2 = -(altitude2 + t2 // 4 * per_cycle)
#             heapq.heappush(heap, (neg_potential2, t2, altitude2, r2, c2))


# answer1 = find_best()
# print(answer1)





import collections
import heapq


with open("./2024/input/everybody_codes_e2024_q20_p1.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])
start_r, start_c = next((r, c) for r, line in enumerate(lines) for c, ch in enumerate(line) if ch == 'S')

delta = {
    'S': -1,
    '.': -1,
    '+': +1,
    '-': -2
}



targets = {(20, c) for c, ch in enumerate(lines[20]) if ch == '+'}

def find_best():
    heap = [(-100, 100, 1000, start_r, start_c)] # neg_potential, t, altitude, r, c
    heapq.heapify(heap)

    seen = {(start_r, start_c)}
    while heap:
        neg_potential, t, altitude, r, c = heapq.heappop(heap)

        if (r, c) in targets:
            print(f'{r,c=} {altitude=}')
            print(f'{t=}')
            return -neg_potential

        for direction in 'NESW':
            r2 = r + (direction == 'S') - (direction == 'N')
            c2 = c + (direction == 'E') - (direction == 'W')
            if not (0 <= r2 < nrows) or not (0 <= c2 < ncols) or lines[r2][c2] == '#' or (r2, c2) in seen:
                continue
            seen.add((r2, c2))
            altitude2 = altitude + delta[lines[r2][c2]]
            t2 = t - 1
            neg_potential2 = -(altitude2 + t2)
            heapq.heappush(heap, (neg_potential2, t2, altitude2, r2, c2))


answer1 = find_best()
print(answer1)


# 67
# Your answer length is: incorrect
# The first character of your answer is: incorrect

# 1034
# CORRECT


# Part 2

import collections

with open("./2024/input/everybody_codes_e2024_q20_p2.txt") as f:
    lines = f.read().splitlines()

# lines = '''###############S###############
# #-----------------------------#
# #-------------+++-------------#
# #-------------+++-------------#
# #-------------+++-------------#
# #-----------------------------#
# #-----------------------------#
# #-----------------------------#
# #--A-----------------------C--#
# #-----------------------------#
# #-----------------------------#
# #-----------------------------#
# #-----------------------------#
# #-----------------------------#
# #-----------------------------#
# #--------------B--------------#
# #-----------------------------#
# #-----------------------------#
# ###############################'''.splitlines()
# # 10000 


nrows = len(lines)
ncols = len(lines[0])

next_target = {}
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == 'S':
            start = (r, c)
            next_target['C'] = ((r, c), 'S')
        elif ch == 'A':
            next_target[None] = ((r, c), 'A')
        elif ch == 'B':
            next_target['A'] = ((r, c), 'B')
        elif ch == 'C':
            next_target['B'] = ((r, c), 'C')

delta = {
    'S': -1,
    'A': -1,
    'B': -1,
    'C': -1,
    '.': -1,
    '+': +1,
    '-': -2
}

valid_directions = {
    'N': 'NEW',
    'E': 'NES',
    'S': 'ESW',
    'W': 'NSW',
}

start_altitude = 10_000

# Checkpoints: None, A, B, C, S



def find_best():
    test = set()

    q = collections.deque([(start_altitude, *start, None, 'S')]) # altitude, r, c, last_checkpoint, direction
    seen = {q[0]}
    d = 0
    while q:
        for _ in range(len(q)):
            altitude, r, c, last_checkpoint, direction = q.popleft()

            # if (last_checkpoint) not in test or (r, c) == (0, 15):
            #     test.add((last_checkpoint))
            #     print(f'{altitude, r, c, last_checkpoint, direction=}')

            for direction2 in valid_directions[direction]:
                r2 = r + (direction2 == 'S') - (direction2 == 'N')
                c2 = c + (direction2 == 'E') - (direction2 == 'W')
                if not (0 <= r2 < nrows) or not (0 <= c2 < ncols) or lines[r2][c2] == '#':
                    continue

                altitude2 = altitude + delta[lines[r2][c2]]
                if altitude2 < start_altitude - 100 or altitude2 > start_altitude + 100:
                    continue
                
                last_checkpoint2 = last_checkpoint
                if (r2, c2) == next_target[last_checkpoint][0]:
                    last_checkpoint2 = next_target[last_checkpoint][1]
                    if last_checkpoint2 == 'S':
                        # print(f'FINAL {altitude2, r2, c2, last_checkpoint2, direction2=}')
                        if altitude2 >= 10_000:
                            return d + 1
                        continue

                if (altitude2, r2, c2, last_checkpoint2, direction2) in seen:
                    continue

                seen.add((altitude2, r2, c2, last_checkpoint2, direction2))
                q.append((altitude2, r2, c2, last_checkpoint2, direction2))
        d += 1


answer2 = find_best()
print(answer2)

















# # Part 3


# with open("./2024/input/everybody_codes_e2024_q20_p3.txt") as f:
#     lines = f.read().splitlines()

# answer3 = 'todo'
# print(answer3)
