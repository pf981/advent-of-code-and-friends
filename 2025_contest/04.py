import re


with open("2025_contest/04.txt") as f:
    lines = f.read().splitlines()


def compute_memory(s):
    return sum(int(c) if c.isdigit() else (ord(c) - ord('A') + 1) for c in s)

answer1 = sum(compute_memory(s) for s in lines)
print(answer1)


# Part 2

answer2 = 0
for line in lines:
    keep = len(line) // 10
    s = line[:keep] + str(len(line) - keep - keep) + line[-keep:]
    answer2 += compute_memory(s)

print(answer2)


# Part 3

answer3 = 0
for line in lines:
    s = []
    count = 1
    char = line[0]

    for c in line[1:] + ';':
        if c != char:
            s.extend(str(count))
            s.append(char)
            count = 0

        char = c
        count += 1

    answer3 += compute_memory(s)

print(answer3)
