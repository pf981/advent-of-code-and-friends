import random
import re

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
# squares = set()
# for move in moves:
cnt = len(squares)
while True:
    for _ in range(10_000_000):
        move = random.choice(list(m))
        x2, y2 = m[move]
        x = (x + x2) // 2
        y = (y + y2) // 2
        squares.add((x, y))
        # print(f"{x=} {y=}")
    if len(squares) == cnt:
        break
    cnt = len(squares)

fire = set()
for (
    x,
    y,
) in squares:
    fire.add((x - 1, y))
    fire.add((x, y - 1))
    fire.add((x, y + 1))
    fire.add((x + 1, y))

fire2 = set()
for x, y in fire:
    # if (x, y) in m.values() or (x, y) in squares:
    if (x, y) in squares:
        continue
    fire2.add((x, y))

answer = len(fire2)
print(answer)
# 16167 wrong
# 15799 wrong

# Your answer length is: correct
# The first character of your answer is: correct
