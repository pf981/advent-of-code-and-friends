with open("./input/2026/07.txt") as f:
    lines = f.read().splitlines()

ops, _, *sushi = lines
sushi = [tuple(map(int, line.split(","))) for line in sushi]
sushi.reverse()

answer = x = y = 0
for op in ops[: len(ops) // 2]:
    x += (op == ">") - (op == "<")
    y += (op == "^") - (op == "v")
    if sushi and (x, y) == sushi[-1]:
        sushi.pop()
        answer += 1

print(answer)
