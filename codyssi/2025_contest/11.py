import string


with open("2025_contest/11.txt") as f:
    lines = f.read().splitlines()

lookup = string.digits + string.ascii_uppercase + string.ascii_lowercase

nums = []
for line in lines:
    s, base = line.split()
    base = int(base)

    num = 0
    for c in s:
        num *= base
        num += lookup.index(c)
    nums.append(num)

answer1 = max(nums)
print(answer1)


# Part 2

def to_str(n, lookup):
    base = len(lookup)
    if n < base:
        return lookup[n]
    else:
        return to_str(n // base, lookup) + lookup[n % base]

target = sum(nums)
lookup2 = lookup + '!@#$%^'

answer2 = to_str(target, lookup2)
print(answer2)


# Part 3

def get_len(n, base):
    if n < base:
        return 1
    else:
        return get_len(n // base, base) + 1

for base in range(2, 10000):
    if get_len(target, base) <= 4:
        answer3 = base
        break

print(answer3)
