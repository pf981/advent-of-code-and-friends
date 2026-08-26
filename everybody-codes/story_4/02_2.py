with open("./story_4/input/everybody_codes_e4_q02_p2.txt") as f:
    lines = f.read().splitlines()

*nodes, moves = lines

moves = moves.split("=")[1]

m = {}
for line in nodes:
    node, pos = line.split("=")
    x, y = map(int, pos[1:-1].split(","))

    if node == "START":
        start = x, y
    else:
        m[node] = (x, y)


x, y = start
squares = {(x, y)}
for move in moves:
    x2, y2 = m[move]
    x = (x + x2) // 2
    y = (y + y2) // 2
    squares.add((x, y))

fire = set()
for x, y in squares:
    for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        if (x + dx, y + dy) in squares:
            continue
        fire.add((x + dx, y + dy))

answer = len(fire)
print(answer)
