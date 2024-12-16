from aocd import get_data, submit
import heapq

inp = get_data(day=16, year=2024)
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
best_score = None
while heap:
    score, r, c, heading = heapq.heappop(heap)
    if (r, c, heading) in seen:
        continue
    seen.add((r, c, heading))

    if (r, c) == end:
        best_score = score
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

answer1 = best_score
print(answer1)

submit(answer1, part='a', day=16, year=2024)


# Part 2


import collections


best_paths = set()
seen = set() # r, c, heading
heap = [(0, start[0], start[1], 'E', frozenset())] # score, r, c, heading, path
to_check = collections.defaultdict(set) # (r, c, heading, score) -> [path, ...]

while heap:
    score, r, c, heading, path = heapq.heappop(heap)
    if (r, c, heading) in seen:
        to_check[(r, c, heading, score)].update(path)
        continue
    seen.add((r, c, heading))

    path = path | {(r, c, heading, score)}

    if (r, c) == end:
        if score == best_score:
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

while True:
    best_paths_copy = best_paths.copy()
    for state in best_paths_copy:
        best_paths.update(to_check[state])
    if best_paths == best_paths_copy:
        break

answer2 = len({(r, c) for r, c, _, _ in best_paths})
print(answer2)

submit(answer2, part='b', day=16, year=2024)
