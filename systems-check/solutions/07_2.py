import collections

with open("./input/7.txt") as f:
    lines = f.read().splitlines()

loads = collections.Counter()
for line in lines:
    id_, p_in, p_out = line.split()
    p_in = int(p_in)
    p_out = int(p_out)

    eff = 100 * p_out // p_in
    if eff < 97:
        s = id_.split("|")[1]
        for i in range(0, len(s), 3):
            load = s[i : i + 3]
            loads[load] += eff

answer = max(loads.values())
print(answer)
