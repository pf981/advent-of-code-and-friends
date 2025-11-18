with open("./2025/input/everybody_codes_e2025_q12_p3.txt") as f:
    lines = f.read().splitlines()

# lines = """5411
# 3362
# 5235
# 3112""".splitlines()

# lines = """41951111131882511179
# 32112222211508122215
# 31223333322105122219
# 31234444432147511128
# 91223333322176021892
# 60112222211166431583
# 04661111166111111746
# 01111119042122222177
# 41222108881233333219
# 71222127839122222196
# 56111026279711111507""".splitlines()

# grid = [int(x) for x in line] for line in lines]
m = {(r, c): int(ch) for r, line in enumerate(lines) for c, ch in enumerate(line)}
import collections

nrows = len(lines)
ncols = len(lines[0])


# Start is list of pos
def get_best(m, start):
    q = collections.deque(start)
    destroyed = set()
    while q:
        r, c = q.popleft()
        if (r, c) not in m:
            continue
        if (r, c) in destroyed:
            continue
        destroyed.add((r, c))

        val = m[(r, c)]
        for dr, dc in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            r2 = r + dr
            c2 = c + dc
            if (r2, c2) not in m or (r2, c2) in destroyed:
                continue
            if m[(r2, c2)] > val:
                continue
            q.append((r2, c2))
    return destroyed


p1 = 0, 0
d1 = set()
for r in range(nrows):
    for c in range(ncols):
        d1x = get_best(m, [(r, c)])
        if len(d1x) > len(d1):
            d1 = d1x
            p1 = (r, c)


m2 = m.copy()
for r, c in d1:
    del m2[(r, c)]

p2 = 0, 0
d2 = set()
for r in range(nrows):
    for c in range(ncols):
        if (r, c) not in m2:
            continue
        d2x = get_best(m2, [(r, c)])
        if len(d2x) > len(d2):
            d2 = d2x
            p2 = (r, c)

m3 = m2.copy()
for r, c in d2:
    if (r, c) in m3:
        del m3[(r, c)]

p3 = 0, 0
d3 = set()
for r in range(nrows):
    for c in range(ncols):
        if (r, c) not in m3:
            continue
        d3x = get_best(m3, [(r, c)])
        if len(d3x) > len(d3):
            d3 = d3x
            p3 = (r, c)

final = get_best(m, [p1, p2, p3])


answer1 = len(final)
print(answer1)


[p1, p2, p3]
# 5797
# Your answer length is: correct
# The first character of your answer is: incorrect
