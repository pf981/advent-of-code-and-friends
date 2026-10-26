with open("./2026/input/everybody_codes_e2026_q01_p3.txt") as f:
    lines = f.read().splitlines()

cones = list(map(int, lines[0].split(",")))

answer = 0
for cone in cones:
    sq = 3
    while sq * sq - 1 < cone:
        sq += 2
    answer += sq * sq - 1 - cone
print(answer)
