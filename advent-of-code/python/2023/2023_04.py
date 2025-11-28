from aocd import get_data, submit
import re


inp = get_data(day=4, year=2023)
cards = [[set(re.findall(r'\d+', side)) for side in line.split(':')[1].split('|')] for line in inp.splitlines()]
n_wins = [len(have.intersection(want)) for have, want in cards]
answer1 = sum(2**(n - 1) for n in n_wins if n > 0)
print(answer1)

submit(answer1, part='a', day=4, year=2023)


# Part 2


import functools


@functools.cache
def count_scratchcards(i):
  if i > len(n_wins):
    return 0

  return 1 + sum(count_scratchcards(i + j + 1) for j in range(n_wins[i]))


answer2 = sum(count_scratchcards(i) for i in range(len(n_wins)))
print(answer2)

submit(answer2, part='b', day=4, year=2023)
