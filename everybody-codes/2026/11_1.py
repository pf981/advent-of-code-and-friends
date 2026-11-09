import collections

with open("./2026/input/everybody_codes_e2026_q11_p1.txt") as f:
    lines = f.read().splitlines()

head, _, *rest = lines

n = int(head.split()[1])

m = {node: [] for node in range(1, n + 1)}
for node in range(1, n):
    m[node].append(node + 1)
    m[node + 1].append(node)
m[n].append(1)
m[1].append(n)


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

s2 = sum(get_route_sum(node) for node in range(1, n + 1))

answer = s1 - s2
print(answer)
