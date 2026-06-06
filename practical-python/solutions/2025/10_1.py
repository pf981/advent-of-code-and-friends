import collections

with open("./input/2025/10/input1.txt") as f:
    text = f.read()
start, end = "S1", "MD"

m = collections.defaultdict(dict)
for line in text.splitlines():
    ab, cap = line.split()
    a, b = ab.split("-")
    m[a][b] = int(cap)
    m[b][a] = 0


def find_augmenting_path(node: int, seen: set[int]) -> tuple[int, ...] | None:
    if node == end:
        return (node,)

    if node in seen:
        return None
    seen.add(node)

    for node2, cap in m[node].items():
        if cap <= 0:
            continue
        if path := find_augmenting_path(node2, seen):
            return (node,) + path


answer = 0
while path := find_augmenting_path(start, set()):
    min_cap = min(m[a][b] for a, b in zip(path[:-1], path[1:]))
    answer += min_cap
    for a, b in zip(path[:-1], path[1:]):
        m[a][b] -= min_cap
        m[b][a] += min_cap

print(answer)
