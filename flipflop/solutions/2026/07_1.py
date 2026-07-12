with open("./input/2026/07.txt") as f:
    lines = f.read().splitlines()
# lines = """>>>^>>v<^<^>>>>v<^^>vv>^<^^^^^<^<vv>^^^>

# 3,0
# 5,1
# 5,0
# 3,2
# 7,1
# 6,1
# 7,3
# 7,1
# 7,6
# 5,8
# 5,7
# 6,6
# 7,9""".splitlines()
ops, _, *lines = lines

sushi = [tuple(map(int, line.split(","))) for line in lines]
sushi.reverse()

x = y = 0
# eat = set()
result = 0
# for op in ops[: len(ops) // 2]:
for op in ops[:2500]:
    x += (op == ">") - (op == "<")
    y += (op == "^") - (op == "v")
    if sushi and (x, y) == sushi[-1]:
        sushi.pop()
        # eat.add((x, y))
        result += 1

answer = result
print(answer)
