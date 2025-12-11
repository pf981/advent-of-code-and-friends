from aocd import get_data, submit
import re
import functools

inp = get_data(day=11, year=2025)
# inp = """svr: aaa bbb
# aaa: fft
# fft: ccc
# bbb: tty
# tty: ccc
# ccc: ddd eee
# ddd: hub
# hub: fff
# eee: dac
# dac: fff
# fff: ggg hhh
# ggg: out
# hhh: out
# """


lines = inp.splitlines()
m = {}
for line in lines:
    from_, *to = re.findall(r"[a-z]{3}", line)
    m[from_] = to


@functools.cache
def count_ways(node, parent, has_dac, has_fft):
    if node == "out":
        return int(has_dac) and int(has_fft)

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
print(answer2)
submit(answer2, part="b", day=11, year=2025)
# 278341040353001229
# not right
