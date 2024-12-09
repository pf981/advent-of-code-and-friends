from aocd import get_data, submit


inp = get_data(day=1, year=2024)
lines = inp.splitlines()

l = []
r = []
for line in lines:
    a, b = line.split()
    l.append(int(a))
    r.append(int(b))

l.sort()
r.sort()

answer1 = sum(abs(b - a) for a, b in zip(l, r))
print(answer1)

submit(answer1, part='a', day=1, year=2024)


# Part 2


import collections


counts = collections.Counter(r)
answer2 = sum(abs(a * counts[a]) for a in l)
print(answer2)

submit(answer2, part='b', day=1, year=2024)
