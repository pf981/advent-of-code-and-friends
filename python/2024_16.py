from aocd import get_data, submit
import heapq

inp = get_data(day=16, year=2024)

# inp = '''###############
# #.......#....E#
# #.#.###.#.###.#
# #.....#.#...#.#
# #.###.#####.#.#
# #.#.#.......#.#
# #.#.#####.###.#
# #...........#.#
# ###.#.#####.#.#
# #...#.....#.#.#
# #.#.#.###.#.#.#
# #.....#...#.#.#
# #.###.#.#.#.#.#
# #S..#.....#...#
# ###############
# '''

lines = inp.splitlines()

walls = set()
start = None
end = None
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == '#':
            walls.add((r, c))
        elif ch == 'S':
            start = r, c
        elif ch == 'E':
            end = r, c

seen = set() # r, c, heading
heap = [(0, start[0], start[1], 'E')] # score, r, c, heading
while heap:
    score, r, c, heading = heapq.heappop(heap)
    # print(score, r, c, heading)
    if (r, c, heading) in seen:
        continue
    seen.add((r, c, heading))

    if (r, c) == end:
        answer1 = score
        break
    
    for heading2 in 'NESW':
        r2 = r + (heading2 == 'S') - (heading2 == 'N')
        c2 = c + (heading2 == 'E') - (heading2 == 'W')
        if (r2, c2, heading) in seen or (r2, c2) in walls:
            continue

        score2 = score + 1

        if heading == heading2:
            pass
        elif heading == 'N':
            if heading2 == 'S':
                score2 += 2000
            else:
                score2 += 1000
        elif heading == 'E':
            if heading2 == 'W':
                score2 += 2000
            else:
                score2 += 1000
        elif heading == 'S':
            if heading2 == 'N':
                score2 += 2000
            else:
                score2 += 1000
        elif heading == 'W':
            if heading2 == 'E':
                score2 += 2000
            else:
                score2 += 1000

        heapq.heappush(heap, (score2, r2, c2, heading2))


best_score = answer1
print(answer1)

# submit(answer1, part='a', day=16, year=2024)


# Part 2

# score = 0
# r, c = start
# heading = 'E'
# cur_path = set()
# best_paths = set()

# def backtrack():
#     global score
#     global r, c
#     global heading
#     # print(f'{r, c, score, heading=}')
#     if (r, c) in cur_path:
#         return
#     cur_path.add((r, c)) #

#     if (r, c) == end:
#         # print(f'Found end {r, c, heading, score=}')
#         if score == best_score:
#             # print(f'New path!')
#             best_paths.update(cur_path)
#         cur_path.remove((r, c))
#         return
    
#     original_score = score
#     original_heading = heading
#     original_r = r
#     original_c = c
    
#     for heading2 in 'NESW':
#         r = original_r + (heading2 == 'S') - (heading2 == 'N')
#         c = original_c + (heading2 == 'E') - (heading2 == 'W')
#         if (r, c) in walls:
#             continue

#         score = original_score + 1

#         if heading == heading2:
#             pass
#         elif heading == 'N':
#             if heading2 == 'S':
#                 score += 2000
#             else:
#                 score += 1000
#         elif heading == 'E':
#             if heading2 == 'W':
#                 score += 2000
#             else:
#                 score += 1000
#         elif heading == 'S':
#             if heading2 == 'N':
#                 score += 2000
#             else:
#                 score += 1000
#         elif heading == 'W':
#             if heading2 == 'E':
#                 score += 2000
#             else:
#                 score += 1000

#         if score > best_score:
#             continue
        
#         heading_original = heading
#         heading = heading2
#         backtrack()
#         heading = heading_original
    
#     score = original_score
#     heading = original_heading
#     r = original_r
#     c = original_c
#     cur_path.remove((r, c))


# backtrack()


# answer2 = len(best_paths)
# print(answer2)

# submit(answer2, part='b', day=16, year=2024)

import collections

best_paths = set()
seen = set() # r, c, heading
heap = [(0, start[0], start[1], 'E', frozenset())] # score, r, c, heading, path

to_check = collections.defaultdict(set) # (r, c, heading, score) -> [path, ...]

while heap:
    score, r, c, heading, path = heapq.heappop(heap)
    # print(score, r, c, heading)
    if (r, c, heading) in seen:
        to_check[(r, c, heading, score)].update(path)
        continue
    seen.add((r, c, heading))

    path = path | {(r, c, heading, score)}

    if (r, c) == end:
        if score == best_score:
            print(f'New path!')
            best_paths.update(path)
        continue
    
    for heading2 in 'NESW':
        r2 = r + (heading2 == 'S') - (heading2 == 'N')
        c2 = c + (heading2 == 'E') - (heading2 == 'W')
        if (r2, c2, heading) in seen or (r2, c2) in walls:
            continue

        score2 = score + 1

        if heading == heading2:
            pass
        elif heading == 'N':
            if heading2 == 'S':
                score2 += 2000
            else:
                score2 += 1000
        elif heading == 'E':
            if heading2 == 'W':
                score2 += 2000
            else:
                score2 += 1000
        elif heading == 'S':
            if heading2 == 'N':
                score2 += 2000
            else:
                score2 += 1000
        elif heading == 'W':
            if heading2 == 'E':
                score2 += 2000
            else:
                score2 += 1000

        if score2 > best_score:
            continue
        heapq.heappush(heap, (score2, r2, c2, heading2, path))

for _ in range(100):
    for state in best_paths.copy():
        best_paths.update(to_check[state])

answer2 = len({(r, c) for r, c, _, _ in best_paths})
print(answer2)

submit(answer2, part='b', day=16, year=2024)
