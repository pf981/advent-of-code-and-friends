import sys

sys.setrecursionlimit(1_000_000)

with open("./story_4/input/everybody_codes_e4_q02_p3.txt") as f:
    lines = f.read().splitlines()

m = {}
for line in lines:
    node, pos = line.split("=")
    pos = tuple(map(int, pos[1:-1].split(",")))

    if node == "START":
        start = pos
    else:
        m[node] = pos

squares = {start}


def dfs(x: int, y: int) -> None:
    for move in "ABC":
        x2, y2 = m[move]
        x3 = (x + x2) // 2
        y3 = (y + y2) // 2

        if (x3, y3) in squares:
            continue

        squares.add((x3, y3))
        dfs(x3, y3)


dfs(*start)

fire = set()
for x, y in squares:
    for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        if (x + dx, y + dy) in squares:
            continue
        fire.add((x + dx, y + dy))

answer = len(fire)
print(answer)
