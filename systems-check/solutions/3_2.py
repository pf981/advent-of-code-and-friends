import itertools

with open("./input/3.txt") as f:
    text = f.read()

part1, part2 = text.split("\n\n")

chunks = list(map(int, part2.split(",")))

nodes = {}  # id_ -> (x, y)
for line in part1.splitlines():
    id_, x, y = line.split()

    if id_ == "#S":
        id_ = 0
    elif id_ == "#D":
        id_ = float("inf")
    else:
        id_ = int(id_[1:])

    x = int(x[1:])
    y = int(y[1:])

    nodes[id_] = (x, y)

dists = {}
m = {}
for id_, (x, y) in nodes.items():
    m[id_] = []
    for id2, (x2, y2) in nodes.items():
        if id2 == id_:
            continue

        d = dists[(id_, id2)] = abs(x2 - x) + abs(y2 - y)
        if d <= 5:
            m[id_].append(id2)

buffers = {id_: [] for id_ in m}
buffers[0] = chunks
seen = {(0, chunk) for chunk in chunks}  # {(node, chunk), ...}
from_order = sorted(buffers)

while True:
    for from_ in from_order:
        to_order = sorted(
            m[from_], key=lambda id_: (dists[(from_, id_)], len(buffers[id_]), id_)
        )
        it = itertools.cycle(to_order)

        new_buffer = []
        for chunk in buffers[from_]:
            for _ in range(len(to_order)):
                to = next(it)
                if (to, chunk) not in seen:
                    seen.add((to, chunk))
                    buffers[to].append(chunk)
                    break
            else:
                new_buffer.append(chunk)

        if buffers[from_] != new_buffer:
            buffers[from_] = new_buffer
            break
    else:
        break

answer = sum(buffers[float("inf")][-5:] * len(buffers[float("inf")]))
print(answer)
