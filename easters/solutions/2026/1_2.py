with open("./input/2026/1.txt") as f:
    text = f.read()

parts = [part.splitlines() for part in text.split("\n\n")]
nrows = len(parts[0])
ncols = len(parts[0][0])


def merge(part1: list[str], part2: list[str]) -> list[str]:
    alive = {(r, c) for r in range(nrows) for c in range(ncols) if part1[r][c] == "#"}
    alive2 = set()

    for r in range(nrows):
        for c in range(ncols):
            neis = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    r2 = r + dr
                    c2 = c + dc
                    if dr == dc == 0 or not (0 <= r2 < nrows and 0 <= c2 < ncols):
                        continue
                    neis += part2[r2][c2] == "#"

            if ((r, c) in alive and neis in [2, 7]) or (
                (r, c) not in alive and neis in [3, 4, 6]
            ):
                alive2.add((r, c))

    alive = alive2

    out = []
    for r in range(nrows):
        line = []
        for c in range(ncols):
            line.append("#" if (r, c) in alive else ".")
        out.append("".join(line))
    return out


for j in range(len(parts)):
    outs = [merge(parts[i], parts[j]) for i in range(6)]
    for out in zip(*outs):
        print(*out)
    print()

answer = 433161
print(answer)
