with open("./input/01.txt") as f:
    txt = f.read()

answer0 = txt.count(".............") // 2
print(answer0)

answer1 = txt.count(".")
print(answer1)

stars = {
    (r, c)
    for r, line in enumerate(txt.splitlines())
    for c, ch in enumerate(line)
    if ch == "."
}

parents = {pos: pos for pos in stars}
counts = {pos: 1 for pos in stars}

P = tuple[int, int]


def union(i: P, j: P) -> None:
    i = find(i)
    j = find(j)
    if i == j:
        return
    if counts[j] < counts[i]:
        i, j = j, i

    parents[i] = j
    counts[j] += counts[i]
    counts[i] = 0


def find(i: P) -> P:
    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]
    return i


for r, c in stars:
    for dr in range(-2, 3):
        for dc in range(-2, 3):
            if abs(dr) + abs(dc) > 2:
                continue
            if dr == dc == 0:
                continue
            if (r + dr, c + dc) not in stars:
                continue

            union((r, c), (r + dr, c + dc))

answer2 = sum(count > 0 for count in counts.values())
print(answer2)
