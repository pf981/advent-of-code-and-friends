import re
import sys

sys.setrecursionlimit(1_000_000)
with open("./story_4/input/everybody_codes_e4_q02_p3.txt") as f:
    lines = f.read().splitlines()
# lines = """START=[5,0]
# A=[0,0]
# B=[10,0]
# C=[5,10]""".splitlines()
# lines = """START=[0,0]
# A=[0,0]
# B=[80,15]
# C=[5,30]""".splitlines()

start, a, b, c = lines
start = tuple(map(int, re.findall(r"-?\d+", start)))
a = tuple(map(int, re.findall(r"-?\d+", a)))
b = tuple(map(int, re.findall(r"-?\d+", b)))
c = tuple(map(int, re.findall(r"-?\d+", c)))

m = {"A": a, "B": b, "C": c}

x, y = start
squares = {(x, y)}

seen = set()


def get_best(x: int, y: int) -> int:
    # print(x, y)
    result = 0
    for move in "ABC":
        x2, y2 = m[move]
        x3 = (x + x2) // 2
        y3 = (y + y2) // 2
        if (x3, y3) in seen:
            continue
        seen.add((x3, y3))
        result = max(result, get_best(x3, y3))
    return 1 + result


# answer = get_best(*start)
get_best(*start)

fire = set()
for (
    x,
    y,
) in seen:
    fire.add((x - 1, y))
    fire.add((x, y - 1))
    fire.add((x, y + 1))
    fire.add((x + 1, y))

fire2 = set()
for x, y in fire:
    # if (x, y) in m.values() or (x, y) in squares:
    if (x, y) in seen:
        continue
    fire2.add((x, y))

answer = len(fire2)
print(answer)
