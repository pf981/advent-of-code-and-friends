with open("./input/11.txt") as f:
    text = f.read()

used: dict[tuple[int, int], int] = {}  # (x, y) -> i
keep = set()

for i, line in enumerate(text.splitlines()[1:]):
    lx, ly, ux, uy = (int(x) for x in line.split(","))
    for x in range(lx, ux):
        for y in range(ly, uy):
            if (x, y) in used:
                keep.add(used[(x, y)])
                keep.add(i)
            else:
                used[(x, y)] = i

answer = sum(i in keep for i in used.values())
print(answer)
