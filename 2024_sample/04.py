import collections


with open("2024_sample/04.txt") as f:
    lines = f.read().splitlines()

m = collections.defaultdict(list)
for line in lines:
    a, _, b = line.split()
    m[a].append(b)
    m[b].append(a)

answer1 = len(m)
print(answer1)


q = collections.deque(['STT'])
seen = {'STT'}
for d in range(3):
    for _ in range(len(q)):
        node = q.popleft()
        for node2 in m[node]:
            if node2 not in seen:
                q.append(node2)
                seen.add(node2)
answer2 = len(seen)
print(answer2)


d = 0
q = collections.deque(['STT'])
seen = {'STT'}
answer3 = 0
while q:
    for _ in range(len(q)):
        node = q.popleft()
        answer3 += d

        for node2 in m[node]:
            if node2 not in seen:
                q.append(node2)
                seen.add(node2)
    d += 1
print(answer3)
