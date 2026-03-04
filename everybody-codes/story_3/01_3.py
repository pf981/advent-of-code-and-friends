import collections

with open("./story_3/input/everybody_codes_e3_q01_p3.txt") as f:
    lines = f.read().splitlines()

counts = collections.Counter()
id_sum = collections.Counter()
for line in lines:
    num, rest = line.split(":")
    r, g, b, s = rest.split()

    r = int(r.replace("r", "0").replace("R", "1"), 2)
    g = int(g.replace("g", "0").replace("G", "1"), 2)
    b = int(b.replace("b", "0").replace("B", "1"), 2)
    s = int(s.replace("s", "0").replace("S", "1"), 2)

    if r > b and r > g:
        dom = "r"
    elif g > r and g > b:
        dom = "g"
    elif b > r and b > g:
        dom = "b"
    else:
        continue

    if s <= 30:
        shine = "matte"
    elif s >= 33:
        shine = "shiny"
    else:
        continue

    group = f"{dom}-{shine}"
    counts[group] += 1
    id_sum[group] += int(num)

answer3 = id_sum[counts.most_common(1)[0][0]]
print(answer3)
