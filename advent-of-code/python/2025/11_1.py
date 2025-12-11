from aocd import get_data, submit
import re
import functools

inp = get_data(day=11, year=2025)
# inp = """aaa: you hhh
# you: bbb ccc
# bbb: ddd eee
# ccc: ddd eee fff
# ddd: ggg
# eee: out
# fff: out
# ggg: out
# hhh: ccc fff iii
# iii: out
# """


lines = inp.splitlines()
m = {}
for line in lines:
    from_, *to = re.findall(r"[a-z]{3}", line)
    m[from_] = to


@functools.cache
def count_ways(node, parent):
    if node == "out":
        return 1

    ways = 0
    for to in m[node]:
        if node == parent:
            continue
        ways += count_ways(to, node)
    return ways


answer1 = count_ways("you", "")
print(answer1)
submit(answer1, part="a", day=11, year=2025)
