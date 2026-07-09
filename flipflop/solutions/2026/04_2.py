with open("./input/2026/04.txt") as f:
    lines = f.read().splitlines()

swaps = 0
is_right = True
for line in lines[::-1]:
    if "o" not in line:
        continue

    if line[0] == "o":
        if is_right:
            is_right = False
            swaps += 1
    else:
        if not is_right:
            is_right = True
            swaps += 1

answer2 = swaps
print(answer2)
