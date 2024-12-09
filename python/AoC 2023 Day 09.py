from aocd import get_data

inp = get_data(day=9, year=2023)

from aocd import get_data, submit


def extrapolate(seq):
    if all(num == 0 for num in seq):
        return 0

    deltas = [b - a for a, b in zip(seq[:-1], seq[1:])]
    return seq[-1] + extrapolate(deltas)


inp = get_data(day=9, year=2023)
seqs = [[int(num) for num in line.split(' ')] for line in inp.splitlines()]
answer1 = sum(extrapolate(seq) for seq in seqs)
print(answer1)

submit(answer1, part='a', day=9, year=2023)


# Part 2


answer2 = sum(extrapolate(seq[::-1]) for seq in seqs)
print(answer2)

submit(answer2, part='b', day=9, year=2023)
