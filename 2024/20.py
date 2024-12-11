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


with open("./2024/input/everybody_codes_e2024_p20_p2.txt") as f:
    lines = f.read().splitlines()

answer2 = 'todo'
print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q20_p3.txt") as f:
    lines = f.read().splitlines()

answer3 = 'todo'
print(answer3)
