def to_coord(r, c):
    x = c
    y = r
    return f"({x}, {y})"


with open("data/2/list-of-instructions.txt") as f:
    instructions = f.read().splitlines()

with open("data/2/map-of-the-tunnels.txt") as f:
    tunnels = f.read().splitlines()

nrows = len(tunnels)
ncols = len(tunnels[0])
start_r, start_c = next(
    (r, c) for r in range(nrows) for c in range(ncols) if tunnels[r][c] == "I"
)

assert to_coord(start_r, start_c) == "(3, 21)"

directions = []
for line in instructions:
    for ch in line:
        if ch not in "NESW":
            continue
        directions.append(ch)

r, c = start_r, start_c
for d in directions:
    r2 = r + (d == "S") - (d == "N")
    c2 = c + (d == "E") - (d == "W")

    if tunnels[r2][c2] == "█":
        continue

    assert tunnels[r2][c2] in "I "

    r, c = r2, c2

answer = to_coord(r, c)
print(answer)
