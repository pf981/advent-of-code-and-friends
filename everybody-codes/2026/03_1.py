import re


def to_dec(left: list[int], right: list[int]) -> int:
    exponent = len(right) - 1
    num = 0
    for a, b in zip(right, left):
        num += a * (b**exponent)
        exponent -= 1
    return num


with open("./2026/input/everybody_codes_e2026_q03_p1.txt") as f:
    lines = f.read().splitlines()

answer = 0
for line in lines:
    nums = list(map(int, re.findall(r"\d", line)))
    mi = len(nums) // 2
    left, right = nums[:mi], nums[mi:]
    answer += to_dec(left, right)

print(answer)
