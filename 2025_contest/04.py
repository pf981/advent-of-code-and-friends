import re


with open("2025_contest/04.txt") as f:
    inp = f.read()

# inp = '''NNBUSSSSSDSSZZZZMMMMMMMM
# PWAAASYBRRREEEEEEE
# FBBOFFFKDDDDDDDDD
# VJAANCPKKLZSSSSSSSSS
# NNNNNNBBVVVVVVVVV'''

answer1 = sum(ord(c) - ord('A') + 1 for c in inp if c != '\n')
print(answer1)


# Part 2

answer2 = 0
for line in inp.splitlines():
    keep = len(line) // 10
    s = line[:keep] + str(len(line) - keep - keep) + line[-keep:]
    memory = sum(int(c) if c.isdigit() else (ord(c) - ord('A') + 1) for c in s)
    answer2 += memory

print(answer2)


# Part 3

# inp = '''NNBUSSSSSDSSZZZZMMMMMMMM
# PWAAASYBRRREEEEEEE
# FBBOFFFKDDDDDDDDD
# VJAANCPKKLZSSSSSSSSS
# NNNNNNBBVVVVVVVVV'''

answer3 = 0
for line in inp.splitlines():
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
    memory = sum(int(c) if c.isdigit() else (ord(c) - ord('A') + 1) for c in s)
    answer3 += memory

print(answer3)
