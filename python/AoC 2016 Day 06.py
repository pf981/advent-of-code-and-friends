from aocd import get_data

inp = get_data(day=6, year=2016)

from collections import Counter

counters = [Counter(''.join(col)).most_common() for col in zip(*inp.split('\n'))]

answer = ''.join(x[0][0] for x in counters)
answer

answer = ''.join(x[-1][0] for x in counters)
answer
