from aocd import get_data, submit
import re


inp = get_data(day=3, year=2024)
lines = inp.splitlines()

answer1 = 0
for line in lines:
    for a, b in re.findall(r'mul\(([0-9]+),([0-9]+)\)', line):
        answer1 += int(a) * int(b)
print(answer1)

submit(answer1, part='a', day=3, year=2024)


# Part 2


answer2 = 0
doing = True
for line in lines:
    for expr in re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", line):
        if expr == 'do()':
            doing = True
        elif expr == "don't()":
            doing = False
        elif doing:
            a, b = re.findall(r'[0-9]+', expr)
            answer2 += int(a) * int(b)
print(answer2)

submit(answer2, part='b', day=3, year=2024)
