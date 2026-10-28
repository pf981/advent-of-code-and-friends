import re

with open("./2026/input/everybody_codes_e2026_q03_p2.txt") as f:
    lines = f.read().splitlines()
# lines = """ISO-3210 7654
# ISO-8742 2468
# ISO-1 1111
# ISO-13 777
# ISO-34 140856
# ISO-789 2465112
# ISO-2341 945""".splitlines()

answer = 0
for line in lines:
    left, right = re.findall("\d+", line)
    left = list(map(int, left))
    right = list(map(int, right))

    left = left * 20
    left = left[-len(right) :]

    exponent = len(right) - 1
    num = 0
    for a, b in zip(right, left):
        num += a * (b**exponent)
        exponent -= 1
    print(f"{left=} {right=} {num=}")
    answer += num

print(answer)
