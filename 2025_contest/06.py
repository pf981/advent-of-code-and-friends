import re


with open("2025_contest/06.txt") as f:
    inp = f.read()

sum(c.isalpha() for c in inp)


# Part 2

answer2 = 0
for c in inp:
    if not c.isalpha():
        continue
    if c.islower():
        answer2 += ord(c) - ord("a") + 1
    else:
        answer2 += ord(c) - ord("A") + 27
print(answer2)


# Part 3

answer3 = 0
prev = 0
for c in inp:
    if not c.isalpha():
        prev = prev * 2 - 5
        while prev < 1:
            prev += 52
        while prev > 52:
            prev -= 52
    else:
        if c.islower():
            prev = ord(c) - ord("a") + 1
        else:
            prev = ord(c) - ord("A") + 27

    answer3 += prev

print(answer3)
