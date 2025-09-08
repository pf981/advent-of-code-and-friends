import collections

with open("./input/11.txt") as f:
    text = f.read()

squares = collections.defaultdict(list)

for i, line in enumerate(text.splitlines()[1:]):
    lx, ly, ux, uy = (int(x) for x in line.split(","))
    for x in range(lx, ux):
        for y in range(ly, uy):
            squares[(x, y)].append(i)

keep = {id_ for ids in squares.values() if len(ids) > 1 for id_ in ids}

answer = 0
for ids in squares.values():
    answer += any(id_ in keep for id_ in ids)

print(answer)
