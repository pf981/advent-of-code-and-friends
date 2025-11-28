from aocd import get_data

inp = get_data(day=6, year=2017)

import itertools

def redistribute(block_counts):
    i = block_counts.index(max(block_counts))
    remaining = block_counts[i]
    block_counts[i] = 0

    while remaining:
        i = (i + 1) % len(block_counts)
        block_counts[i] += 1
        remaining -= 1

def count_cycles(block_counts):
    block_counts = block_counts.copy()
    seen = {}
    for cycles in itertools.count():
        h = tuple(block_counts)
        if h in seen:
            return cycles, cycles - seen[h]
        seen[h] = cycles

        redistribute(block_counts)

block_counts = [int(x) for x in inp.split('\t')]
cycles, loop_size = count_cycles(block_counts)

answer = cycles
print(answer)

answer = loop_size
print(answer)
