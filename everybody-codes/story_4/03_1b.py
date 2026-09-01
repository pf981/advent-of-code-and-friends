with open("./story_4/input/everybody_codes_e4_q03_p1.txt") as f:
    lines = f.read().splitlines()

for line in lines:
    if line.startswith("width"):
        width = int(line.split("=")[1])
    elif line.startswith("height"):
        height = int(line.split("=")[1])
    elif line.startswith("horizontal-offsets"):
        horizontal_offs = list(map(int, line.split("=")[1]))
    elif line.startswith("vertical-offsets"):
        vertical_offs = list(map(int, line.split("=")[1]))
    else:
        assert False

nrows = height
ncols = width

answer = 0
for r in range(nrows):
    for c in range(ncols):
        n = c % 2 == horizontal_offs[r % len(horizontal_offs)]
        e = r % 2 == vertical_offs[(c + 1) % len(vertical_offs)]
        s = c % 2 == horizontal_offs[(r + 1) % len(horizontal_offs)]
        w = r % 2 == vertical_offs[c % len(vertical_offs)]

        answer += n and e and s and w

print(answer)
