with open("./2025/input/everybody_codes_e2025_q01_p1.txt") as f:
    lines = f.read().splitlines()

names = lines[0].split(",")
instructions = lines[2].split(",")

i = 0
for direction, *d in instructions:
    i += int("".join(d)) * (-1 if direction == "L" else 1)
    if i >= len(names):
        i = len(names) - 1
    if i <= 0:
        i = 0

answer1 = names[i]
print(answer1)


# Part 2


with open("./2025/input/everybody_codes_e2025_q01_p2.txt") as f:
    lines = f.read().splitlines()

names = lines[0].split(",")
instructions = lines[2].split(",")

i = 0
for direction, *d in instructions:
    i += int("".join(d)) * (-1 if direction == "L" else 1)

answer2 = names[i % len(names)]
print(answer2)


# Part 3


with open("./2025/input/everybody_codes_e2025_q01_p3.txt") as f:
    lines = f.read().splitlines()

names = lines[0].split(",")
instructions = lines[2].split(",")

i = 0
for direction, *d in instructions:
    j = int("".join(d)) * (-1 if direction == "L" else 1)
    j = j % len(names)
    names[i], names[j] = names[j], names[i]

answer3 = names[0]
print(answer3)
