with open("2025_contest/08.txt") as f:
    inp = f.read()

# inp = """tv8cmj0i2951190z5w44fe205k542l5818ds05ib425h9lj260ud38-l6a06
# a586m0eeuqqvt5-k-8434hb27ytha3i75-lw23-0cj856l7zn8234a05eron"""

answer1 = sum(c.isalpha() for c in inp)
print(answer1)


# Part 2
import re

answer2 = 0
for line in inp.splitlines():
    for _ in range(100):
        line = re.sub(r"[-a-zA-Z]\d", "", line)
        line = re.sub(r"\d[-a-zA-Z]", "", line)
    answer2 += len(line)

print(answer2)

# answer2 = 0
# for line in inp.splitlines():
#     alpha_count = number_count = 0
#     answer2 += len(line)
#     for c in line:
#         if c.isalpha() or c == "-":
#             if number_count:
#                 number_count -= 1
#                 answer2 -= 1
#             else:
#                 alpha_count += 1
#         elif c.isdigit():
#             if alpha_count:
#                 alpha_count -= 1
#                 answer2 -= 1
#             else:
#                 number_count += 1
#         else:
#             alpha_count = number_count = 0
#         print(f'{c=} {alpha_count=} {number_count=}')

# print(answer2)


# Part 3

answer3 = 0
for line in inp.splitlines():
    for _ in range(100):
        line = re.sub(r"[a-zA-Z]\d", "", line)
        line = re.sub(r"\d[a-zA-Z]", "", line)
    answer3 += len(line)

print(answer3)
