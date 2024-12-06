with open("./2024/input/everybody_codes_e2024_q12_p1.txt") as f:
    lines = f.read().splitlines()

# lines = '''.............
# .C...........
# .B......T....
# .A......T.T..
# ============='''.splitlines()

floor = len(lines) - 1

def shoot(r, c, power):
    for _ in range(power):
        r -= 1
        c += 1
        yield r, c
    for _ in range(power):
        c += 1
        yield r, c
    while r < floor:
        r += 1
        c += 1
        yield r, c

def does_hit(start_row, start_col, target_row, target_col, power):
    return (target_row, target_col) in shoot(start_row, start_col, power)


# for r, c in shoot(1, 1, 3):
#     print(r, c)


targets = []
starts = [] # [(row, col, c)]
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c in '.=':
            continue
        if c == 'T':
            targets.append((row, col))
        else:
            starts.append((c, row, col))

ranking_value = 0
for target_row, target_col in targets:
    for power in range(1, len(lines[0])):
        for c, start_row, start_col in starts:
            if does_hit(start_row, start_col, target_row, target_col, power):
                ranking_value += {'A': 1, 'B': 2, 'C': 3}[c] * power
                break
        else:
            continue
        break
    else:
        print(f'Could not hit target {target_row}, {target_col}')

answer1 = ranking_value
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q12_p2.txt") as f:
    lines = f.read().splitlines()

# lines = '''.............
# .C...........
# .B......H....
# .A......T.H..
# ============='''.splitlines()

floor = len(lines) - 1

targets = []
starts = [] # [(row, col, c)]
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c in '.=':
            continue
        if c == 'T':
            targets.append((row, col))
        elif c == 'H':
            targets.append((row, col))
            targets.append((row, col))
        else:
            starts.append((c, row, col))

ranking_value = 0
for target_row, target_col in targets:
    for power in range(1, len(lines[0])):
        for c, start_row, start_col in starts:
            if does_hit(start_row, start_col, target_row, target_col, power):
                ranking_value += {'A': 1, 'B': 2, 'C': 3}[c] * power
                break
        else:
            continue
        break
    else:
        print(f'Could not hit target {target_row}, {target_col}')

answer2 = ranking_value
print(answer2)


# Part 3


# with open("./2024/input/everybody_codes_e2024_q12_p3.txt") as f:
#     lines = f.read().splitlines()

# meteors = [(int(line.split()[0]), int(line.split()[1])) for line in lines]

# max(list(zip(*meteors))[0])
# max(list(zip(*meteors))[1])
# min(list(zip(*meteors))[0])
# min(list(zip(*meteors))[1])

# answer3 = 'todo'
# print(answer3)
