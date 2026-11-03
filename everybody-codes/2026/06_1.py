import collections

with open("./2026/input/everybody_codes_e2026_q06_p1.txt") as f:
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

ingredients = set()
def dfs(ingredient: str) -> None:
    print(f'{ingredient=}')
    if ingredient in ingredients:
        return
    ingredients.add(ingredient)
    for ing2 in m[ingredient]:
        dfs(ing2)

dfs("NULL")
answer = len(ingredients) - 1
print(answer)
