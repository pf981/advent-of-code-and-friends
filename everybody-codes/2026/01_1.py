with open("./2026/input/everybody_codes_e2026_q01_p1.txt") as f:
    lines = f.read().splitlines()

cones = list(map(int, lines[0].split(",")))

answer = 0
for cone in cones:
    sq = 1
    while sq * sq < cone:
        sq += 1
    answer += sq * sq - cone
print(answer)
