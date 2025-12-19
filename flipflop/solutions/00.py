import collections


with open("./input/00.txt") as f:
    lines = f.read().splitlines()

nums = [int(line) for line in lines]
answer1 = sum(nums)
print(answer1)


answer2 = round(sum(nums) / len(nums))
print(answer2)


most_common_num = collections.Counter(nums).most_common(1)[0][0]
digit_counts = collections.Counter("".join(lines))
least_common_digit = min(digit_counts, key=lambda digit: digit_counts[digit])
answer3 = f"{most_common_num}{least_common_digit}"
print(answer3)
