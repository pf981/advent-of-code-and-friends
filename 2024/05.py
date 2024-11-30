import collections
import itertools


with open("./2024/input/everybody_codes_e2024_q05_p1.txt") as f:
    lines = f.read().splitlines()

columns = list(zip(*([int(num) for num in line.split(' ')] for line in lines)))
columns = [list(column) for column in columns]
n = len(columns)

for round in range(10):
    i = round % len(columns)
    num = columns[i].pop(0)
    columns[(i + 1) % n].insert(num - 1, num)

answer1 = ''.join(str(column[0]) for column in columns)
print(answer1)


# Part 2


with open("./2024/input/everybody_codes_e2024_q05_p2.txt") as f:
    lines = f.read().splitlines()

columns = list(zip(*([int(num) for num in line.split(' ')] for line in lines)))
columns = [list(column) for column in columns]
n = len(columns)
counts = collections.Counter()

for round in itertools.count(1):
    i = (round - 1) % len(columns)
    num = columns[i].pop(0)

    next_column = columns[(i + 1) % n]

    j = num - 1
    left_to_right = (j // len(next_column)) % 2 == 0
    j = j % len(next_column)

    if left_to_right:
        next_column.insert(j, num)
    else:
        next_column.insert(len(next_column) - j, num)
    
    s = ''.join(str(column[0]) for column in columns)
    counts[s] += 1
    if counts[s] == 2024:
        answer2 = int(s) * round
        break

print(answer2)


# Part 3


with open("./2024/input/everybody_codes_e2024_q05_p3.txt") as f:
    lines = f.read().splitlines()

columns = list(zip(*([int(num) for num in line.split(' ')] for line in lines)))
columns = [list(column) for column in columns]
n = len(columns)
counts = collections.Counter()

best = 0
seen = set()

for round in itertools.count(1):
    i = (round - 1) % len(columns)
    num = columns[i].pop(0)

    next_column = columns[(i + 1) % n]

    j = num - 1
    left_to_right = (j // len(next_column)) % 2 == 0
    j = j % len(next_column)

    if left_to_right:
        next_column.insert(j, num)
    else:
        next_column.insert(len(next_column) - j, num)
    
    best = max(best, int(''.join(str(column[0]) for column in columns)))
    tup = (i, tuple(tuple(tuple(col) for col in columns)))
    if tup in seen:
        answer3 = best
        break
    seen.add(tup)

print(answer3)
