import itertools


def count_bingos(cube, call) -> int:
    bingos = 0
    pos = next(
        (
            (x, y, z, p)
            for x, y, z, p in itertools.product(range(5), repeat=4)
            if cube[x][y][z][p] == call
        ),
        None,
    )
    if pos is None:
        return 0

    x0, y0, z0, p0 = pos
    cube[x0][y0][z0][p0] = -1

    for dx, dy, dz, dp in itertools.product((-1, 0, 1), repeat=4):
        if dx == dy == dz == dp == 0:
            continue

        # Go to edge
        x, y, z, p = x0, y0, z0, p0
        while True:
            x -= dx
            y -= dy
            z -= dz
            p -= dp
            if not (0 <= x < 5 and 0 <= y < 5 and 0 <= z < 5 and 0 <= p < 5):
                break

        # Count from edge
        marked = 0
        while True:
            x += dx
            y += dy
            z += dz
            p += dp
            if not (0 <= x < 5 and 0 <= y < 5 and 0 <= z < 5 and 0 <= p < 5):
                break
            marked += cube[x][y][z][p] == -1

        assert 1 <= marked <= 5
        if marked >= 5:
            bingos += 1

    return bingos // 2


with open("./input/2026/12.txt") as f:
    text = f.read()

host, cards_s = text.split("\n\n")
host = list(map(int, host.split()))

cubes = []
lines = cards_s.splitlines()
for i in range(0, len(lines), 5):
    cube = []
    for j in range(5):
        nums = list(map(int, lines[i + j].split()))
        batch = itertools.batched(nums, 5)
        cube.append([list(b) for b in batch])
    cubes.append(cube)

bingos = 0
for i, call in enumerate(host, 1):
    bingos += count_bingos(cubes, call)
    if bingos >= 5:
        break

answer = call
print(answer)
