import collections


def find_best_path(lines: list[str]) -> tuple[str]:
    m = collections.defaultdict(list)
    for line in lines:
        a, b = line.split(':')
        for c in b.split(','):
            m[a].append(c)

    q = collections.deque([('RR',)])
    while q:
        candidates = []
        for _ in range(len(q)):
            path = q.popleft()
            node = path[-1]
            if node == '@':
                candidates.append(path)
                continue
            for node2 in m[node]:
                q.append(path + (node2,))
        if len(candidates) == 1:
            return candidates[0]


with open("./2024/input/everybody_codes_e2024_q06_p1.txt") as f:
    lines = f.read().splitlines()

path = find_best_path(lines)
answer1 = ''.join(path)
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q06_p2.txt") as f:
    lines = f.read().splitlines()

path = find_best_path(lines)
answer2 = ''.join(node[0] for node in path)
print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q06_p3.txt") as f:
    lines = f.read().splitlines()

path = find_best_path(lines)
answer3 = ''.join(node[0] for node in path)
print(answer3)
