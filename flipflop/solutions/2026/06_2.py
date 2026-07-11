with open("./input/2026/06.txt") as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])
start = next((r, c) for r in range(nrows) for c in range(ncols) if lines[r][c] == "S")
gears = {(r, c) for r in range(nrows) for c in range(ncols) if lines[r][c] in "#3"}
lights = {(r, c) for r in range(nrows) for c in range(ncols) if lines[r][c] == "*"}
b_in = {
    (r, c): ch
    for r in range(nrows)
    for c in range(ncols)
    if (ch := lines[r][c]).islower()
}
b_out = {
    ch.lower(): (r, c)
    for r in range(nrows)
    for c in range(ncols)
    if (ch := lines[r][c]).isupper()
}

seen = {start}
stack = [(*start, False)]
result = []
while stack:
    r, c, is_clockwise = stack.pop()
    for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        r2 = r + dr
        c2 = c + dc
        if (r2, c2) in seen:
            continue
        seen.add((r2, c2))

        if (r2, c2) in lights:
            result.append((r2, c2, is_clockwise))

        if (r2, c2) in gears:
            stack.append((r2, c2, not is_clockwise))
        if (r2, c2) in b_in:
            stack.append((*b_out[b_in[(r2, c2)]], is_clockwise))

result.sort()
answer = int("".join(str(int(c)) for _, _, c in result), 2)
print(answer)
