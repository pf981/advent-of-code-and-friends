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


with open("./2024/input/everybody_codes_e2024_q12_p3.txt") as f:
    lines = f.read().splitlines()

# lines = '''6 5
# 6 7
# 10 5'''.splitlines()

meteors = [[int(num) for num in line.split()] for line in lines]


def shoot(power):
    y = 0
    yield y
    for _ in range(power):
        y += 1
        yield y
    for _ in range(power):
        yield y
    while True:
        y -= 1
        yield y


def get_y(target_x, power):
    return next((y for x, y in enumerate(shoot(power)) if x == target_x))

# best_hit: (y, power)
# t_meteor >= t
# Basically, get the point furthest right where the projectile isn't past the meteor yet
# But isn't that just the MIDDLE? So you need any point BEFORE the middle
# So x <= meteor_start_x // 2
# I think we are guaranteed one of our starts will hit at x//2
def power_to_hit(x: int, y: int) -> int | None:
    l = 0
    r = x
    while l <= r:
        m = (l + r) // 2
        cur_y = get_y(x, m)
        if cur_y == y:
            return m
        elif cur_y < y:
            l = m + 1
        else:
            r = m - 1
    return None

# meteor_x = 6
# meteor_y = 5
# x_hit = meteor_x // 2
# y_hit = meteor_y - x_hit
# start_y = 2
# power_to_hit(x_hit, y_hit - start_y)

answer3 = 0
for meteor_x, meteor_y in meteors:
    x_hit = meteor_x // 2
    y_hit = meteor_y - x_hit

    print(f'{x_hit=} {y_hit=}')

    ranking_value = float('inf')
    for start_y in range(3):
        power = power_to_hit(x_hit, y_hit - start_y)
        # print(f'{power=}')
        if power is not None:
            ranking_value = min(ranking_value, power * (start_y + 1))
    # print(f'{meteor_x, meteor_y=}{ranking_value=}')
    answer3 += ranking_value

print(answer3)

# 731907
# Your answer length is: correct
# The first character of your answer is: correct

# get_y(1, 99)

# list(shoot(1))

# # answer3 = 'todo'
# # print(answer3)

# power_to_hit(6, 5)

# ranking_value = {'A': 1, 'B': 2, 'C': 3}[c] * power

power_to_hit(10, 5)
power_to_hit(10, 5-1)
power_to_hit(10, 5-2)

meteor_x=10
meteor_y=5



# 997
# Your answer length is: incorrect
# The first character of your answer is: incorrect