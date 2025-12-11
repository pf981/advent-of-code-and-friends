from aocd import get_data, submit
import re
import functools

inp = get_data(day=11, year=2025)
lines = inp.splitlines()

m = {}
for line in lines:
    from_, *to = re.findall(r"[a-z]{3}", line)
    m[from_] = to


@functools.cache
def count_ways(node: str, parent: str) -> int:
    if node == "out":
        return 1

    ways = 0
    for to in m[node]:
        if node == parent:
            continue
        ways += count_ways(to, node)
    return ways


answer1 = count_ways("you", "")
submit(answer1, part="a", day=11, year=2025)
