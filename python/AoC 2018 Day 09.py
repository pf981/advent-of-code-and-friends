from aocd import get_data

inp = get_data(day=9, year=2018)

import collections
import re

def calculate_high_score(players, points):
  marbles = collections.deque([0])
  scores = collections.defaultdict(int)
  
  for new_marble in range(1, points + 1):
    if new_marble % 23 == 0:
      marbles.rotate(7)
      scores[new_marble % players] += new_marble + marbles[0]
      marbles.popleft()
    else:
      marbles.rotate(-2)
      marbles.appendleft(new_marble)
  return max(scores.values())

players, points = (int(x) for x in re.findall(r'\d+', inp))

answer = calculate_high_score(players, points)
print(answer)

answer = calculate_high_score(players, points * 100)
print(answer)
