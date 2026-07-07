import collections
import heapq

with open("input/05.txt") as f:
    text = f.read()

MOD = 10**9 + 7
n_m, *lines = text.splitlines()

n, n_edges = map(int, n_m.split())
m = collections.defaultdict(list)
for line in lines:
    u, v, w = map(int, line.split())
    m[u].append((v, w))

dist_a = [-1] * (n + 1)
heap = [(0, 1)]
while heap:
    d, node = heapq.heappop(heap)

    if dist_a[node] != -1:
        continue
    dist_a[node] = d

    for node2, w in m[node]:
        heapq.heappush(heap, (d + w, node2))


def get_dist(b: int) -> int:
    seen = set()
    heap = [(0, b)]
    best = dist_a[b]
    if best == -1:
        return -1

    while heap:
        d, node = heapq.heappop(heap)

        if node in seen:
            continue
        seen.add(node)

        best = min(best, d + dist_a[node])

        for node2, w in m[node]:
            heapq.heappush(heap, (d + w, node2))

    return best


answer = sum(get_dist(node) for node in range(2, n + 1)) % MOD
print(answer)
