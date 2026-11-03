
import random
import collections
import functools

def solve():
    with open("./2026/input/everybody_codes_e2026_q06_p3.txt") as f:
        lines = f.read().splitlines()
    # lines ='''MEAL:BRDS,CAKE,DOUG
    # BRDS:DOUG,FLWR
    # CAKE:DOUG,FLWR,NULLv2,NULLv3
    # DOUG:FLWR,YSTS,SLTT,NULLv1
    # FLWR:BRDS,DOUG
    # YSTS:SPCS
    # SOUP:BRDS,CAKE,DOUG,FLWR'''.splitlines()

    m = collections.defaultdict(list)
    for line in lines:
        out, in_ = line.split(":")
        assert not out.startswith("NULL")
        m[out].extend(in_.split(","))

    visiting = set()
    visited = {}

    def topo_sort(ing: str) -> bool:
        if ing.startswith("NULL"):
            visited[ing] = {ing}
            return

        if ing in visiting:
            return
        elif ing in visited:
            return
        
        visiting.add(ing)
        visited[ing] = set()
        l = m[ing].copy()
        random.shuffle(l)
        # for ing2 in m[ing]:
        for ing2 in l:
            topo_sort(ing2)
            visited[ing].update(visited[ing2])
        visiting.remove(ing)

    nodes = set(m)
    for l in m.values():
        for node in l:
            nodes.add(node)
    for node in nodes:
        topo_sort(node)
    # null_nodes = [node for node in nodes if node.startswith("NULL")]

    # answer = 0
    # answer = sum(len(visited[ing]) >= 2 for ing in visited if not ing.startswith("NULL"))
    # print(answer)
    # return answer
    return {ing for ing in visited if not ing.startswith("NULL") and len(visited[ing]) >= 2}

res = set()
for _ in range(1000):
    res.update(solve())
answer = len(res)
print(answer)
# 1421 Wrong