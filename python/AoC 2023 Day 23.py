from aocd import get_data

inp = get_data(day=23, year=2023)

from aocd import get_data, submit


def get_longest_hike(m, target):
    stack = [((0, 1), 0)]
    longest_hike = 0
    seen = set()

    while stack:
        pos, d = stack.pop()
        
        if pos not in m or m[pos] == '#':
            continue

        if pos == target:
            longest_hike = max(longest_hike, d)

        if (pos) in seen:
            continue
        seen.add((pos))

        for direction in '<>^v':
            if m[pos] in '<>^v' and direction != m[pos]:
                continue

            new_pos = (
                pos[0] + (direction == 'v') - (direction == '^'),
                pos[1] + (direction == '>') - (direction == '<')
            )

            if new_pos not in m:
                continue
            if m[new_pos] == dict(zip('^>v<', 'v<^>'))[direction]:
                continue

            stack.append((new_pos, d + 1))
    return longest_hike


inp = get_data(day=23, year=2023)
lines = inp.splitlines()
m = {(row, col): c for row, line in enumerate(lines) for col, c in enumerate(line)}
target = (len(lines) - 1, len(lines[0]) - 2)

answer1 = get_longest_hike(m, target)
print(answer1) # 1 minute

submit(answer1, part='a', day=23, year=2023)


# Part 2


import collections


def get_adjacencies(m, pos):
    adjacencies = []

    for direction in '^>v<':
        new_pos = (
            pos[0] + (direction == 'v') - (direction == '^'),
            pos[1] + (direction == '>') - (direction == '<')
        )

        if new_pos in m and m[new_pos] != '#':
            adjacencies.append(new_pos)
    
    return adjacencies


def get_edges(m, target):
    edges = collections.defaultdict(list) # pos -> [(pos, d), ...]

    stack = [((0, 1), (1, 1), 1)] # prev_node, pos, d
    visited = set()
    while stack:
        prev_node, pos, d = stack.pop()

        if (prev_node, pos) in visited:
            continue
        visited.add((prev_node, pos))

        adjacencies = get_adjacencies(m, pos)
        new_d = d + 1

        if pos == target:
            edges[prev_node].append((pos, d))
            continue

        if len(adjacencies) > 2:
            edges[prev_node].append((pos, d))
            prev_node = pos
            new_d = 1

        for new_pos in adjacencies:
            stack.append((prev_node, new_pos, new_d))
    
    return edges


def get_longest_hike2(m, target):
    edges = get_edges(m, target) # pos -> pos, d

    start_pos = (0, 1)
    stack = [(start_pos, 0, frozenset())]
    longest_hike = 0
    while stack:
        pos, d, visited = stack.pop()

        if pos == target:
            longest_hike = max(longest_hike, d)
            continue

        if (pos) in visited:
            continue
        visited = visited.union(set([pos]))

        for new_pos, d2 in edges[pos]:
            stack.append((new_pos, d + d2, visited))

    return longest_hike


lines = inp.splitlines()
m = {(row, col): c for row, line in enumerate(lines) for col, c in enumerate(line)}
target = (len(lines) - 1, len(lines[0]) - 2)

answer2 = get_longest_hike2(m, target)
print(answer2) # 1 minute

submit(answer2, part='b', day=23, year=2023)
