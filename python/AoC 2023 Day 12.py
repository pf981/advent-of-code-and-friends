from aocd import get_data

inp = get_data(day=12, year=2023)

from aocd import get_data, submit
import functools


@functools.cache
def counts(conditions, rls):
    if not conditions:
        if rls:
            return 0
        return 1

    if conditions[0] == '#':
        if not rls:
            return 0
        i = 0
        while i < rls[0]:
            if i >= len(conditions) or conditions[i] not in '#?':
                return 0
            i += 1
        if i < len(conditions) and conditions[i] == '#':
            return 0
        return counts(conditions[i+1:], rls[1:]) # +1 because need a gap

    if conditions[0] == '.':
        return counts(conditions[1:], rls)
    
    # It is ?
    return counts('#' + conditions[1:], rls) + counts('.' + conditions[1:], rls)


inp = get_data(day=12, year=2023)
reports = [(conditions, tuple([int(r) for r in rl.split(',')])) for conditions, rl in [line.split(' ') for line in inp.splitlines()]]
answer1 = sum(counts(conditions, rls) for conditions, rls in reports)
print(answer1)

submit(answer1, part='a', day=12, year=2023)


# Part 2


answer2 = sum(counts('?'.join([conditions] * 5), rls * 5) for conditions, rls in reports)
print(answer2)

submit(answer2, part='b', day=12, year=2023)
