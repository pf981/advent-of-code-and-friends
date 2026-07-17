import itertools


# If a single number is 2+ bingos on a single card, does it count twice?
def count_bingos(cube, call) -> bool:
    bingos = 0
    pos = next(
        (
            (x, y, z, p)
            for x in range(5)
            for y in range(5)
            for z in range(5)
            for p in range(5)
            if cube[x][y][z][p] == call
        ),
        None,
    )
    if pos is None:
        return False
    # print("found")

    x0, y0, z0, p0 = pos
    cube[x0][y0][z0][p0] = -1

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                for dp in [-1, 0, 1]:
                    if dx == dy == dz == dp == 0:
                        continue

                    # Go to edge
                    x, y, z, p = x0, y0, z0, p0
                    while True:
                        x -= dx
                        y -= dy
                        z -= dz
                        p -= dp
                        if not (
                            0 <= x < 5 and 0 <= y < 5 and 0 <= z < 5 and 0 <= p < 5
                        ):
                            break

                    # Count from edge
                    marked = 0
                    while True:
                        x += dx
                        y += dy
                        z += dz
                        p += dp
                        if not (
                            0 <= x < 5 and 0 <= y < 5 and 0 <= z < 5 and 0 <= p < 5
                        ):
                            break
                        marked += cube[x][y][z][p] == -1

                    assert 1 <= marked <= 5
                    if marked >= 5:
                        bingos += 1

    # return min(bingos, 1)  # FIXME
    # return bingos
    return bingos // 2  # FIXME: TEST


with open("./input/2026/12.txt") as f:
    text = f.read()
# text = """62 121 64 51 86 85 36 31 8 113 71 72 75 101 115 44 52 78 26 80 116 98 79 17 77
# 110 91 10 9 55 74 107 67 93 54 81 25 58 82 56 5 89 32 14 119 48 35 109 47 21
# 6 69 40 92 68 18 105 66 41 90 22 30 63 57 15 28 125 76 49 65 123 20 16 99 24
# 108 96 53 87 60 38 73 59 94 83 100 33 111 46 4 106 124 27 104 84 88 42 1 118 12
# 70 37 39 112 19 7 97 11 114 95 3 120 50 2 61 117 122 102 13 45 103 29 34 23 43

# 82 39 88 103 71 76 108 109 104 34 49 58 85 107 121 105 67 18 77 118 30 117 26 29 55
# 6 43 23 96 100 2 47 11 37 24 4 73 120 81 60 112 106 12 92 57 1 54 16 40 31
# 13 17 3 111 78 56 115 102 124 33 8 122 75 61 25 89 64 20 119 46 113 87 116 44 53
# 66 38 94 91 36 93 5 45 32 62 42 69 63 28 14 72 86 74 79 9 50 84 80 35 41
# 10 97 21 83 70 48 90 7 125 15 52 22 51 101 99 19 68 110 114 123 27 65 95 98 59"""

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
# 81 incorrect
# len(hcube[0][0][0][0][0])
# len(cubes[0][0][0])
