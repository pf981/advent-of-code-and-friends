with open("./story_4/input/everybody_codes_e4_q02_p1.txt") as f:
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

answer = len(squares)
print(answer)
