import collections
import functools

with open("./2026/input/everybody_codes_e2026_q06_p3.txt") as f:
    lines = f.read().splitlines()
lines ='''MEAL:BRDS,CAKE,DOUG
BRDS:DOUG,FLWR
CAKE:DOUG,FLWR,NULLv2,NULLv3
DOUG:FLWR,YSTS,SLTT,NULLv1
FLWR:BRDS,DOUG
YSTS:SPCS
SOUP:BRDS,CAKE,DOUG,FLWR'''.splitlines()

m = collections.defaultdict(set)
parents = {}
for line in lines:
    out, ins = line.split(":")
    assert not out.startswith("NULL")
    for in_ in ins.split(","):
        m[out].add(in_)
        parents[in_] = out

nodes = set(m) | set(parents)
stack = [node for node in nodes if node not in m]
nulls = collections.defaultdict(set)
for node in stack:
    nulls[node] = {node}

while stack:
    node = stack.pop()
    print(f'{node=}')
    p = parents[node]
    m[p].remove(node)
    nulls[p].update(nulls[node])
    if not m[p]:
        stack.append(p)

answer = sum(len(nulls[node]) >= 2 for node in nulls)
print(answer)