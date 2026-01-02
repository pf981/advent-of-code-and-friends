import collections
import functools


with open("data/day14.txt") as f:
    text = f.read()

start, *lines = text.splitlines()
start = start.split()[1]

m = collections.defaultdict(list)
for line in lines:
    a, b, c = line.split()
    a = a[:-1]
    m[b].append((a, 1))
    m[c].append((a, 0))


@functools.cache
def count_ins(node: str) -> int:
    if node == start:
        return 12**3456

    return sum((count_ins(parent) + extra) // 2 for parent, extra in m[node])


MOD = 10**15
answer = count_ins("OUT") % MOD
print(answer)
