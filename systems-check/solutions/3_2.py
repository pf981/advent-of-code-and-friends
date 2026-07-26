import itertools

with open("./input/3.txt") as f:
    text = f.read()
# text = """#S X1 Y0
# #1 X5 Y1
# #2 X8 Y2
# #3 X9 Y6
# #D X9 Y9

# 4,5,2,3,1"""
# text = """#S X1 Y0
# #1 X3 Y3
# #2 X5 Y1
# #3 X8 Y2
# #4 X9 Y6
# #5 X10 Y1
# #D X9 Y9

# 9,10,5,3,4,1,8,2,6,7"""

part1, part2 = text.split("\n\n")

chunks = list(map(int, part2.split(",")))

nodes = {}  # id_ -> (x, y)
for line in part1.splitlines():
    id_, x, y = line.split()
    id_ = id_[1:]
    if id_ == "S":
        id_ = "0"
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
buffers["0"] = chunks
seen = {("0", chunk) for chunk in chunks}  # {(node, chunk), ...}
from_order = sorted(buffers)

while True:
    # print(buffers)
    # print()
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
                # Put chunk back into cur node
                new_buffer.append(chunk)

        if buffers[from_] != new_buffer:
            buffers[from_] = new_buffer
            break
    else:
        break

print(buffers)
answer = sum(buffers["D"][-5:] * len(buffers["D"]))
print(answer)
# 15125 incorrect
