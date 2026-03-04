with open("./story_3/input/everybody_codes_e3_q01_p2.txt") as f:
    lines = f.read().splitlines()

vals = []
for line in lines:
    num, rest = line.split(":")
    r, g, b, s = rest.split()

    r = int(r.replace("r", "0").replace("R", "1"), 2)
    g = int(g.replace("g", "0").replace("G", "1"), 2)
    b = int(b.replace("b", "0").replace("B", "1"), 2)
    s = int(s.replace("s", "0").replace("S", "1"), 2)

    vals.append((s, -(r + g + b), int(num)))

answer2 = max(vals)[2]
print(answer2)
