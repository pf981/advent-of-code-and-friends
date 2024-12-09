from aocd import get_data

inp = get_data(day=14, year=2015)

import re

def get_winner(t):
  winner_names = []
  winner_distance = float('-inf')
  for line in inp.split('\n'):
    name, speed, flight_time, rest_time = (f(x) for f, x in zip((str, int, int, int), re.search(r'(\w+).*?(\d+).*?(\d+).*?(\d+)', line).groups()))

    d_round = t // (flight_time + rest_time) * (flight_time * speed)
    d_extra = min(t % (flight_time + rest_time), flight_time) * speed
    d = d_round + d_extra

    if d > winner_distance:
      winner_names = [name]
      winner_distance = d
    elif d == winner_distance:
      winner_names += [name]
  return (winner_names, winner_distance)
  
_, answer = get_winner(2503)
answer

from collections import defaultdict

scores = defaultdict(int)

for t in range(1, 2503+1):
  winner_names, _ = get_winner(t)
  for winner_name in winner_names:
    scores[winner_name] += 1

answer = max(scores.values())
answer
