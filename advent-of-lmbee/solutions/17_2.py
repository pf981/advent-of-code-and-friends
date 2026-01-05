import collections

with open("data/day17.txt") as f:
    text = f.read()

ins = collections.Counter()
outs = collections.Counter()
nodes = set()
for line in text.splitlines():
    a, b = map(int, line.split(" -> "))
    outs[a] += 1
    ins[b] += 1

    nodes.add(a)
    nodes.add(b)

heads = sum(ins[node] == 0 for node in nodes)
leaves = sum(outs[node] == 0 for node in nodes)

answer = max(heads, leaves)
print(answer)
