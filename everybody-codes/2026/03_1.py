import re

with open("./2026/input/everybody_codes_e2026_q03_p1.txt") as f:
    lines = f.read().splitlines()
# lines = """ISO-3210 7654
# ISO-8742 2468
# ISO-1111 1111""".splitlines()

answer = 0
for line in lines:
    nums = list(map(int, re.findall("\d", line)))
    mi = len(nums) // 2
    left, right = nums[:mi], nums[mi:]

    exponent = 3
    num = 0
    for a, b in zip(right, left):
        num += a * (b**exponent)
        exponent -= 1
    print(f"{left=} {right=} {num=} {nums=}")
    answer += num

print(answer)
