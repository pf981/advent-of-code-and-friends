import itertools

with open("./story_3/input/everybody_codes_e3_q02_p1.txt") as f:
    lines = f.read().splitlines()

for r, line in enumerate(lines):
    for c, ch in enumerate(line):
        if ch == "@":
            source = r, c
        if ch == "#":
            bones = r, c

seen = {source}
it = itertools.cycle("NESW")
answer1 = 0
r, c = source
for dir in it:
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
