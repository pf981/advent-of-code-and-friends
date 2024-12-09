from aocd import get_data

inp = get_data(day=15, year=2015)

import re
from functools import reduce
from operator import mul

coefs = list(zip(*[[int(x) for x in re.findall(r'-?\d+', line)] for line in inp.split('\n')]))

def dot_product(l1, l2):
  return sum(x * y for x, y in zip(l1, l2))

total_score_max = float('-inf')
total_score_max_500_calories = float('-inf')
for a in range(100):
  for b in range(100):
    for c in range(100):
      d = 100 - a - b - c
      if d >= 0:
        cookie_scores = [max(dot_product([a,b,c,d], coef), 0) for coef in coefs[:-1]]
        total_score = reduce(mul, cookie_scores, 1)
        total_score_max = max(total_score, total_score_max)
        if dot_product([a,b,c,d], coefs[-1]) == 500:
          total_score_max_500_calories = max(total_score, total_score_max_500_calories)

answer = total_score_max
answer

answer = total_score_max_500_calories
answer
