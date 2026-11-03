import collections
import functools

with open("./2026/input/everybody_codes_e2026_q06_p2.txt") as f:
    lines = f.read().splitlines()
# lines ='''BRDS:FLWR,SLTT,YSTS
# FLWR:SLTT,YSTS
# SLTT:YSTS,MLKK,BTTR
# NULL:BRDS,FLWR,SLTT
# YSTS:BRDS,FLWR
# MLKK:SPCS,NULL
# HNYN:BRDS,FLWR,SLTT,YSTS'''.splitlines()

m = collections.defaultdict(list)
for line in lines:
    out, in_ = line.split(":")
    m[out].extend(in_.split(","))

visiting = set()
visited = {}

def has_null(ing: str) -> bool:
    if ing == "NULL":
        return True
    if ing in visited:
        return visited[ing]
    if ing in visiting:
        return False
    
    visiting.add(ing)

    for ing2 in m[ing]:
        if has_null(ing2):
            visited[ing] = True
            return True
    visited[ing] = False
    return False


answer = sum(has_null(ingredient) for ingredient in m.copy())
print(answer)
