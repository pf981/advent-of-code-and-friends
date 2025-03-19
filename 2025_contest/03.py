import re


with open("2025_contest/03.txt") as f:
    inp = f.read()

nums = [int(b) - int(a) + 1 for a, b in re.findall(r'(\d+)-(\d+)', inp)]

answer1 = sum(nums)
print(answer1)


# Part 2

piles = []
for line in inp.splitlines():
    a, b, c, d = (int(num) for num in re.findall(r'\d+', line))
    piles.append(set(range(a, b + 1)) | set(range(c, d + 1)))

answer2 = sum(len(pile) for pile in piles)
print(answer2)


# Part 3

answer3 = max(len(piles[i] | piles[i + 1]) for i in range(len(piles) - 1))
print(answer3)
