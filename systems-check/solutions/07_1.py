with open("./input/7.txt") as f:
    lines = f.read().splitlines()

answer = 0
for line in lines:
    id_, p_in, p_out = line.split()
    p_in = int(p_in)
    p_out = int(p_out)

    eff = 100 * p_out // p_in
    if eff < 97:
        answer += eff

print(answer)
