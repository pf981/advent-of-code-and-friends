with open("./2025/input/everybody_codes_e2025_q11_p1.txt") as f:
    lines = f.read().splitlines()

columns = [int(line) for line in lines]
is_phase_1 = True
for round in range(11):
    if is_phase_1:
        is_phase_1 = False
        for i in range(0, len(columns) - 1):
            if columns[i] > columns[i + 1]:
                is_phase_1 = True
                columns[i] -= 1
                columns[i + 1] += 1
    else:
        for i in range(0, len(columns) - 1):
            if columns[i + 1] > columns[i]:
                columns[i] += 1
                columns[i + 1] -= 1

answer1 = sum(i * col for i, col in enumerate(columns, 1))
print(answer1)


# Part 2


with open("./2025/input/everybody_codes_e2025_q11_p2.txt") as f:
    lines = f.read().splitlines()

columns = [int(line) for line in lines]
is_phase_1 = True
rnd = -1
while is_phase_1:
    is_phase_1 = False
    for i in range(0, len(columns) - 1):
        if columns[i] > columns[i + 1]:
            is_phase_1 = True
            columns[i] -= 1
            columns[i + 1] += 1
    rnd += 1

target = sum(columns) // len(columns)
for c in columns:
    if target - c > 0:
        rnd += target - c

answer2 = rnd
print(answer2)


# Part 3


with open("./2025/input/everybody_codes_e2025_q11_p3.txt") as f:
    lines = f.read().splitlines()

columns = [int(line) for line in lines]

target = sum(columns) // len(columns)
answer3 = sum(delta for col in columns if (delta := target - col) > 0)
print(answer3)
