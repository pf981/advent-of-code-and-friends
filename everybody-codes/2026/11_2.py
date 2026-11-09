import collections

with open("./2026/input/everybody_codes_e2026_q11_p2.txt") as f:
    lines = f.read().splitlines()

head, _, *rest = lines

n = int(head.split()[1])

m = {node: [] for node in range(1, n + 1)}
for node in range(1, n):
    for i in range(-3, 3 + 1):
        if i == 0:
            continue
        node2 = (node - 1 + i) % n + 1
        m[node].append(node2)
        m[node2].append(node)


def get_route_sum(start) -> int:
    route_sum = 0
    q = collections.deque([start])
    seen = {start}
    d = 0
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            for node2 in m[node]:
                if node2 in seen:
                    continue
                seen.add(node2)
                q.append(node2)
        d += 1
        route_sum += d * len(q)
    return route_sum


s1 = sum(get_route_sum(node) for node in range(1, n + 1))

for line in rest:
    a, b = map(int, line.split())
    m[a].append(b)
    m[b].append(a)

min_s2 = float("inf")

for a in range(1, n + 1):
    for b in range(a + 1, n + 1):
        if a in m[b]:
            continue
        m[a].append(b)
        m[b].append(a)
        s2 = sum(get_route_sum(node) for node in range(1, n + 1))
        min_s2 = min(min_s2, s2)
        m[a].pop()
        m[b].pop()

answer = s1 - min_s2
print(answer)
