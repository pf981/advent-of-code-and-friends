import functools
import re

from aocd import get_data, submit


inp = get_data(day=11, year=2025)
lines = inp.splitlines()

m = {}
for line in lines:
    from_, *to = re.findall(r"[a-z]{3}", line)
    m[from_] = to


@functools.cache
def count_ways(node: str, parent: str, has_dac: bool, has_fft: bool) -> int:
    if node == "out":
        return int(has_dac and has_fft)

    if node == "dac":
        has_dac = True
    if node == "fft":
        has_fft = True

    ways = 0
    for to in m[node]:
        if node == parent:
            continue
        ways += count_ways(to, node, has_dac, has_fft)
    return ways


answer2 = count_ways("svr", "", False, False)
submit(answer2, part="b", day=11, year=2025)
