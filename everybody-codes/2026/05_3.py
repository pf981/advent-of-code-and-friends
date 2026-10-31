with open("./2026/input/everybody_codes_e2026_q05_p3.txt") as f:
    lines = f.read().splitlines()
# lines = """010100100100001101000
# 111101001000001110000
# 101111011000101010011
# 001000101010000100000
# 000110100110011001100
# 000001110111111000000
# 101100010101011110000
# 001101100000001010011
# 001001001111010001001
# 100011011110011010101
# 001100101110010010000""".splitlines()
grid = [list(map(int, line)) for line in lines]
nrows = len(lines)
ncols = len(lines[0])
neighbours = [[0] * ncols for _ in range(nrows)]
for r in range(nrows):
    for c in range(ncols):
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == dc == 0:
                    continue
                r2 = r + dr
                c2 = c + dc
                if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                    continue
                neighbours[r][c] += grid[r2][c2]


def pp():
    for r in range(nrows):
        for c in range(ncols):
            ch = grid[r][c]
            if (r, c) in land:
                ch = "#"
            if (r, c) in sand:
                ch = "="
            print(ch, end="")
        print()
    print()


todo = [(nrows // 2, ncols // 2)]
land = set()
while todo:
    r, c = todo.pop()
    if (r, c) in land:
        continue
    land.add((r, c))

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == dc == 0:
                continue
            r2 = r + dr
            c2 = c + dc
            if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                continue

            neighbours[r2][c2] += 1 - grid[r][c]
            if neighbours[r2][c2] >= 5:
                todo.append((r2, c2))
    # pp()

sand_neighbours = [[0] * ncols for _ in range(nrows)]

todo = []

for r, c in land:
    neis = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == dc == 0:
                continue
            r2 = r + dr
            c2 = c + dc
            if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                continue
            neis += (r2, c2) in land
    if neis < 8:
        todo.append((r, c))

sand = set()
while todo:
    r, c = todo.pop()
    if (r, c) in sand:
        continue
    sand.add((r, c))

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == dc == 0:
                continue
            r2 = r + dr
            c2 = c + dc
            if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                continue

            sand_neighbours[r2][c2] += 1
            if (r2, c2) in land and sand_neighbours[r2][c2] >= 5:
                todo.append((r2, c2))
    # pp()


# Tree stamps

for p in sand:
    land.remove(p)

trees = set()


def is_tree(r, c):
    if (r, c) not in land:
        return False

    for dr in range(-2, 3):
        for dc in range(-2, 3):
            if abs(dr) == abs(dc) == 2:
                continue
            r2 = r + dr
            c2 = c + dc
            if (r2, c2) not in land:
                return False
    return True


for r, c in land:
    if is_tree(r, c):
        trees.add((r, c))


def step():
    global trees
    trees2 = set()

    for r, c in land:
        if sand_neighbours[r][c]:  # TODO: Check this is still correct
            continue
        neis = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == dc == 0:
                    continue
                r2 = r + dr
                c2 = c + dc
                if not (0 <= r2 < nrows and 0 <= c2 < ncols):
                    continue

                neis += (r2, c2) in trees

        if neis >= 4 or (r, c) in trees:
            trees2.add((r, c))

    trees = trees2


step()
step()


answer = len(trees)
print(answer)
