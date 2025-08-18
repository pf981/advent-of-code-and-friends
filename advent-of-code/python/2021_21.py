from aocd import get_data

inp = get_data(day=21, year=2021)

def roll_three():
  result = 0
  for _ in range(3):
    roll_three.die += 1
    result += roll_three.die

  return result


def get_scores(p1, p2):
  p1_score = p2_score = 0
  while True:
    p1 = (p1 - 1 + roll_three()) % 10 + 1
    p1_score += p1
    if p1_score >= 1000:
      return p1_score, p2_score

    p2 = (p2 - 1 + roll_three()) % 10 + 1
    p2_score += p2
    if p2_score >= 1000:
      return p1_score, p2_score


roll_three.die = 0
p1_start, p2_start = (int(line[-1]) for line in inp.splitlines())
p1_score, p2_score = get_scores(p1_start, p2_start)

answer = min(p1_score, p2_score) * roll_three.die
print(answer)

import functools


@functools.lru_cache(maxsize=None)
def sum_wins(p1, p2, p1_score, p2_score, turn):
  if p1_score >= 21:
    return 1, 0
  elif p2_score >= 21:
    return 0, 1
  
  total1 = total2 = 0
  for roll1 in [1, 2, 3]:
      for roll2 in [1, 2, 3]:
          for roll3 in [1, 2, 3]:
            roll = roll1 + roll2 + roll3
            if turn == 1:
              new_p1 = (p1 - 1 + roll) % 10 + 1
              t1, t2 = sum_wins(new_p1, p2, p1_score + new_p1, p2_score, 2)
            else:
              new_p2 = (p2 - 1 + roll) % 10 + 1
              t1, t2 = sum_wins(p1, new_p2, p1_score, p2_score + new_p2, 1)
            total1 += t1
            total2 += t2
            
  return total1, total2


sum_wins.cache_clear()

answer = max(sum_wins(p1_start, p2_start, 0, 0, 1))
print(answer)
