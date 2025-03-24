import re


with open("2025_contest/08.txt") as f:
    inp = f.read()

answer1 = sum(c.isalpha() for c in inp)
print(answer1)


# Part 2

answer2 = 0
for line in inp.splitlines():
    for _ in range(100):
        line = re.sub(r"[-a-zA-Z]\d", "", line)
        line = re.sub(r"\d[-a-zA-Z]", "", line)
    answer2 += len(line)

print(answer2)


# Part 3

answer3 = 0
for line in inp.splitlines():
    for _ in range(100):
        line = re.sub(r"[a-zA-Z]\d", "", line)
        line = re.sub(r"\d[a-zA-Z]", "", line)
    answer3 += len(line)

print(answer3)
