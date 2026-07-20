import functools

with open("./input/3.txt") as f:
    text = f.read()

part1, part2 = text.split("\n\n")

nodes = {}  # id_ -> (x, y)
for line in part1.splitlines():
    id_, x, y = line.split()
    id_ = id_[1:]
    x = int(x[1:])
    y = int(y[1:])

    nodes[id_] = (x, y)

m = {}
for id_, (x, y) in nodes.items():
    m[id_] = []
    for id2, (x2, y2) in nodes.items():
        if id2 == id_:
            continue

        if abs(x2 - x) + abs(y2 - y) <= 5:
            m[id_].append(id2)


@functools.cache
def count_ways(node: str, seen: frozenset[str]) -> int:
    if node == "D":
        return 1

    seen2 = seen | {node}

    ways = 0
    for node2 in m[node]:
        if node2 in seen:
            continue
        ways += count_ways(node2, seen2)
    return ways


answer = count_ways("S", frozenset())
print(answer)
