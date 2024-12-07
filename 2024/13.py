import collections
import heapq


with open("./2024/input/everybody_codes_e2024_q13_p1.txt") as f:
    lines = f.read().splitlines()

# lines = '''#######
# #6769##
# S50505E
# #97434#
# #######'''.splitlines()

# m = collections.defaultdict(lambda: -1)
m = {}
start = None # r, c
end = None # r, c
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c in '# ':
            continue
        if c == 'S':
            start = row, col
            m[(row, col)] = 0
        elif c == 'E':
            end = row, col
            m[(row, col)] = 0
        else:
            m[(row, col)] = int(c)

heap = [(0, *start)] # d, r, c
answer1 = None
seen = set()
while heap:
    d, r, c = heapq.heappop(heap)
    # print(f'{d=} {r=} {c=}')
    if (r, c) == end:
        answer1 = d
        break

    if (r, c) in seen:
        continue
    seen.add((r, c))

    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc
        if (r2, c2) not in m:
            continue
        d2 = min(
            abs(m[(r, c)] - m[(r2, c2)]),
            abs(m[(r, c)] - m[(r2, c2)] - 10),
            abs(m[(r, c)] - m[(r2, c2)] + 10)
        )
        heapq.heappush(heap, (1 + d + d2, r2, c2))

print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q13_p2.txt") as f:
    lines = f.read().splitlines()

m = {}
start = None # r, c
end = None # r, c
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c in '# ':
            continue
        if c == 'S':
            start = row, col
            m[(row, col)] = 0
        elif c == 'E':
            end = row, col
            m[(row, col)] = 0
        else:
            m[(row, col)] = int(c)

heap = [(0, *start)] # d, r, c
answer2 = None
seen = set()
while heap:
    d, r, c = heapq.heappop(heap)
    # print(f'{d=} {r=} {c=}')
    if (r, c) == end:
        answer2 = d
        break

    if (r, c) in seen:
        continue
    seen.add((r, c))

    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc
        if (r2, c2) not in m:
            continue
        d2 = min(
            abs(m[(r, c)] - m[(r2, c2)]),
            abs(m[(r, c)] - m[(r2, c2)] - 10),
            abs(m[(r, c)] - m[(r2, c2)] + 10)
        )
        heapq.heappush(heap, (1 + d + d2, r2, c2))

print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q13_p3.txt") as f:
    lines = f.read().splitlines()


m = {}
starts = []
end = None # r, c
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c in '# ':
            continue
        if c == 'S':
            starts.append((row, col))
            m[(row, col)] = 0
        elif c == 'E':
            end = row, col
            m[(row, col)] = 0
        else:
            m[(row, col)] = int(c)

heap = [(0, *start) for start in starts] # d, r, c
answer3 = None
seen = set()
while heap:
    d, r, c = heapq.heappop(heap)
    # print(f'{d=} {r=} {c=}')
    if (r, c) == end:
        answer3 = d
        break

    if (r, c) in seen:
        continue
    seen.add((r, c))

    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc
        if (r2, c2) not in m:
            continue
        d2 = min(
            abs(m[(r, c)] - m[(r2, c2)]),
            abs(m[(r, c)] - m[(r2, c2)] - 10),
            abs(m[(r, c)] - m[(r2, c2)] + 10)
        )
        heapq.heappush(heap, (1 + d + d2, r2, c2))

print(answer3)

