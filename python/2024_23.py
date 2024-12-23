from aocd import get_data, submit


inp = get_data(day=23, year=2024)

# inp = '''kh-tc
# qp-kh
# de-cg
# ka-co
# yn-aq
# qp-ub
# cg-tb
# vc-aq
# tb-ka
# wh-tc
# yn-cg
# kh-ub
# ta-co
# de-co
# tc-td
# tb-wq
# wh-td
# ta-ka
# td-qp
# aq-cg
# wq-ub
# ub-vc
# de-ta
# wq-aq
# wq-vc
# wh-yn
# ka-de
# kh-ta
# co-tc
# wh-qp
# tb-vc
# td-yn
# '''

lines = inp.splitlines()

import collections
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
print(triples)
len(triples)

answer1 = 0
for a, b, c in triples:
    if a.startswith('t') or b.startswith('t') or c.startswith('t'):
        answer1 += 1
print(answer1)

# submit(answer1, part='a', day=23, year=2024)

def is_group(group):
    for a in group:
        if not (len(m[a].intersection(group)) >= len(group) - 1):
            return False
    return True



import itertools

candidates = set()
for a, s in m.items():
    candidates.add(frozenset(s) | {a})

def solve():
    seen = set()
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

best = solve()

answer2 = ','.join(sorted(best))
submit(answer2, part='b', day=23, year=2024)


# final = set()
# for a, s in m.items():
#     for b in s:
#         best = s.copy()
#         cur = best.intersection(m[b])
#         cur.add(a)
#         cur.add(b)
#         if len(cur) > len(final):
#             print(f'{a=} {b=} {cur=}')
#             final = cur
# final

# # m['co']

# m['vc']
# m['wq']
# m['tb']
# 1
# answer2 = 'todo'
# print(answer2)

# submit(answer2, part='b', day=23, year=2024)












### PART 2



# parents = {}
# def union(a, b):
#     a = find(a)
#     b = find(b)
#     parents[a] = b

# def find(a):
#     while parents[a] != a:
#         parents[a] = parents[parents[a]]
#         a = parents[a]
#     return a

# # nodes = set()

# for line in lines:
#     a, b = line.split('-')
#     parents[a] = a
#     parents[b] = b
#     # nodes.add(a)
#     # nodes.add(b)

# for line in lines:
#     a, b = line.split('-')
#     union(a, b)
    
# groups = collections.defaultdict(list)
# for node, parent in parents.items():
#     groups[parent].append(node)

# nodes = None
# largest = 0
# for group in groups.values():
#     if len(group) > largest:
#         nodes = group
#         largest = len(group)

# largest
# answer2 = ','.join(sorted(nodes))
# # submit(answer2, part='b', day=23, year=2024)




# len(parents)

# answer1 = 0
# for line in inp.splitlines():
#     if ',t' in ',' + line:
#         answer1 += 1

# lines = inp.splitlines()

# answer1 = 'todo'
# print(answer1)

# # submit(answer1, part='a', day=23, year=2024)


# Part 2


# answer2 = 'todo'
# print(answer2)

# submit(answer2, part='b', day=23, year=2024)
