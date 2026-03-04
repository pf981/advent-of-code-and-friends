with open("./story_3/input/everybody_codes_e3_q01_p1.txt") as f:
    lines = f.read().splitlines()

answer1 = 0
for line in lines:
    num, rest = line.split(":")
    r, g, b = rest.split()

    r = int(r.replace("r", "0").replace("R", "1"), 2)
    g = int(g.replace("g", "0").replace("G", "1"), 2)
    b = int(b.replace("b", "0").replace("B", "1"), 2)

    if g > r and g > b:
        answer1 += int(num)

print(answer1)
