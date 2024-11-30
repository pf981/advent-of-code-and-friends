import collections

with open("./2024/input/everybody_codes_e2024_q06_p1.txt") as f:
    lines = f.read().splitlines()

# lines = '''RR:A,B,C
# A:D,E
# B:F,@
# C:G,H
# D:@
# E:@
# F:@
# G:@
# H:@'''.splitlines()

m = collections.defaultdict(list)
for line in lines:
    a, b = line.split(':')
    for c in b.split(','):
        m[a].append(c)
print(f'{m=}')

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
        answer1 = candidates[0]
        break

answer1 = ''.join(answer1)
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q06_p2.txt") as f:
    lines = f.read().splitlines()


m = collections.defaultdict(list)
for line in lines:
    a, b = line.split(':')
    for c in b.split(','):
        m[a].append(c)
# print(f'{m=}')

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
        answer2 = candidates[0]
        break

answer2 = ''.join(c[0] for c in answer2)


print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q06_p3.txt") as f:
    lines = f.read().splitlines()

m = collections.defaultdict(list)
for line in lines:
    a, b = line.split(':')
    for c in b.split(','):
        m[a].append(c)
# print(f'{m=}')

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
        answer3 = candidates[0]
        break

answer3 = ''.join(c[0] for c in answer3)
print(answer3)
