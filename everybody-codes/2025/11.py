with open("./2025/input/everybody_codes_e2025_q11_p1.txt") as f:
    lines = f.read().splitlines()

# lines = """9
# 1
# 1
# 4
# 9
# 6""".splitlines()

columns = [int(line) for line in lines]
is_phase_1 = True
for round in range(11):
    # print(f"{round=} {columns=}")
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
# answer1 = "todo"
print(answer1)


# # Part 2


with open("./2025/input/everybody_codes_e2025_q11_p2.txt") as f:
    lines = f.read().splitlines()

# lines = """9
# 1
# 1
# 4
# 9
# 6""".splitlines()

# lines = """805
# 706
# 179
# 48
# 158
# 150
# 232
# 885
# 598
# 524
# 423""".splitlines()

import itertools

columns = [int(line) for line in lines]
is_phase_1 = True
round = 0
while True:
    if is_phase_1:
        is_phase_1 = False
        for i in range(0, len(columns) - 1):
            if columns[i] > columns[i + 1]:
                is_phase_1 = True
                columns[i] -= 1
                columns[i + 1] += 1

    if not is_phase_1:
        for i in range(0, len(columns) - 1):
            if columns[i + 1] > columns[i]:
                columns[i] += 1
                columns[i + 1] -= 1

    round += 1
    # print(f"{round=} {columns=}")
    if len(set(columns)) == 1:
        break

answer2 = round - 1

print(answer2)

# 5109772

# Your answer length is: correct
# The first character of your answer is: correct

# Next try 5109773 CORRECT (dont subtract one)

# 49

# Your answer length is: incorrect
# The first character of your answer is: incorrect

# # Part 3


import itertools

# with open("./2025/input/everybody_codes_e2025_q11_p2.txt") as f:
#     lines = f.read().splitlines()

with open("./2025/input/everybody_codes_e2025_q11_p3.txt") as f:
    lines = f.read().splitlines()

# lines = """9
# 1
# 1
# 4
# 9
# 6""".splitlines()

# lines = """805
# 706
# 179
# 48
# 158
# 150
# 232
# 885
# 598
# 524
# 423""".splitlines()

# non-dec
# lines = """3 4 4 4 7 8""".split()


columns = [int(line) for line in lines]

# There is no phase 1
# columns_at_phase_2 = columns.copy()  # TODO
# rounds_in_phase_1 = ...

target = sum(columns) // len(columns)
max(columns)

# 5 rounds to balance (6+5=11)
ans = 0
for c in columns:
    if target - c > 0:
        # print(target - c)
        ans += target - c
print(ans)
