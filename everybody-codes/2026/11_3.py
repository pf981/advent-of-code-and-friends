import collections
import itertools


def get_pairs(lst, n=2):
    if not lst:
        yield []
        return

    for group in (((lst[0],) + xs) for xs in itertools.combinations(lst[1:], n - 1)):
        for groups in get_pairs([x for x in lst if x not in group], n):
            yield [group] + groups


with open("./2026/input/everybody_codes_e2026_q11_p3.txt") as f:
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

gap = n // 8
for start in range(1, gap + 1):
    nodes = list(range(start, n + 1, gap))

    for pairs in get_pairs(nodes):
        is_valid = True
        for a, b in pairs:
            if a in m[b]:
                is_valid = False

            m[a].append(b)
            m[b].append(a)

        if is_valid:
            s2 = sum(get_route_sum(node) for node in range(1, n + 1))
            min_s2 = min(min_s2, s2)

        for a, b in pairs:
            m[a].pop()
            m[b].pop()

answer = s1 - min_s2
print(answer)
