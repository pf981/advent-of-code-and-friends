with open("./2026/input/everybody_codes_e2026_q01_p2.txt") as f:
    lines = f.read().splitlines()

cones = list(map(int, lines[0].split(",")))

answer = 0
for cone in cones:
    sq = 3
    while 4 * sq - 4 < cone:
        sq += 1
    answer += 4 * sq - 4 - cone
print(answer)
