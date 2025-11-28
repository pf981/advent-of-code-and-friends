from aocd import get_data, submit
import collections


inp = get_data(day=23, year=2024)
lines = inp.splitlines()

m = collections.defaultdict(set)
for line in lines:
    a, b = line.split('-')
    m[a].add(b)
    m[b].add(a)

triples = set()
for a, l in m.items():
    for b in l:
        for c in m[b]:
            if c in l:
                triples.add(tuple(sorted((a, b, c))))

answer1 = 0
for a, b, c in triples:
    if a.startswith('t') or b.startswith('t') or c.startswith('t'):
        answer1 += 1
print(answer1)

submit(answer1, part='a', day=23, year=2024)


# Part 2


import itertools


def is_group(group):
    for a in group:
        if not (len(m[a].intersection(group)) >= len(group) - 1):
            return False
    return True

def solve():
    candidates = set()
    for a, s in m.items():
        candidates.add(frozenset(s) | {a})

    w = max(len(s) for s in candidates)
    while w > 1:
        for candidate in candidates:
            if len(candidate) < w:
                continue
            if len(candidate) == w:
                if is_group(candidate):
                    return candidate
                continue
            for comb in itertools.combinations(candidate, w):
                if is_group(comb):
                    return comb
        w -= 1


answer2 = ','.join(solve())
print(answer2)

submit(answer2, part='b', day=23, year=2024)
