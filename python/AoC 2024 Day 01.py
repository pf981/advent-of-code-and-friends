from aocd import get_data, submit

inp = get_data(day=1, year=2024)

# FIXME: REMOVE
# inp = '''3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3'''

lines = inp.splitlines()

l = []
r = []
for line in lines:
    a, b = line.split('   ')
    l.append(int(a))
    r.append(int(b))

l.sort()
r.sort()

answer1 = 0
for a, b in zip(l, r):
    answer1 += abs(b - a)

print(answer1)

# submit(answer1, part='a', day=1, year=2024)


# Part 2
import collections
answer2 = 0
cnts = collections.Counter(r)
for a in l:
    answer2 += abs(a * cnts[a])

print(answer2)

# submit(answer2, part='b', day=1, year=2024)
