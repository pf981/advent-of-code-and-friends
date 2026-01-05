import collections
import functools

with open("data/day17.txt") as f:
    text = f.read()

m = collections.defaultdict(list)
for line in text.splitlines():
    a, b = map(int, line.split(" -> "))
    m[a].append(b)


@functools.cache
def get_longest_chain(node: int) -> int:
    result = 1
    for node2 in m[node]:
        result = max(result, 1 + get_longest_chain(node2))

    return result


answer = max(get_longest_chain(node) for node in list(m))
print(answer)
