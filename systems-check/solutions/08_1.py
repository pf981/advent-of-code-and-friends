import functools

with open("./input/8.txt") as f:
    text = f.read()

part1, _ = text.split("\n\n")

m = {}  # node -> (node2, d)
non_roots = set()
for line in part1.splitlines():
    node1 = line[:3]
    node2 = line[-3:]
    d = int(line.split("[")[1].split("]")[0])

    m[node1] = (node2, d)
    non_roots.add(node2)


@functools.cache
def get_dist(node: int) -> int:
    if node not in m:
        return 0

    node2, d = m[node]

    return d + get_dist(node2)


answer = float("inf")
for node in m:
    if node in non_roots:
        continue
    answer = min(answer, get_dist(node))

print(answer)
