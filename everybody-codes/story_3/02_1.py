import itertools

with open("./story_3/input/everybody_codes_e3_q02_p1.txt") as f:
    lines = f.read().splitlines()
# lines = """.......
# .......
# .......
# .#.@...
# .......
# .......
# .......""".splitlines()

# source, bones
for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == "@":
            source = r, c
        if ch == "#":
            bones = r, c

r, c = source
seen = {(r, c)}
it = itertools.cycle("NESW")
answer1 = 0
for dir in it:
    # print(f"{r=} {c=} {seen=}")
    r2 = r + (dir == "S") - (dir == "N")
    c2 = c + (dir == "E") - (dir == "W")
    if (r2, c2) in seen:
        continue
    seen.add((r2, c2))

    r, c = r2, c2
    answer1 += 1
    if (r, c) == bones:
        break

print(answer1)
