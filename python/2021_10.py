from aocd import get_data

inp = get_data(day=10, year=2021)

close_to_error_score = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}
open_to_close = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>'
}
close_to_score = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}

def get_scores(line):
  expected_closes = []
  for c in line:
    if c in ')]}>':
      if c != expected_closes.pop():
        return close_to_error_score[c], None
    else:
      expected_closes += open_to_close[c]
      
  score = 0
  for c in expected_closes[::-1]:
    score *= 5
    score += close_to_score[c]
  
  return None, score
      
scores = [get_scores(line) for line in inp.splitlines()]
error_scores = [error_score for error_score, _ in scores if error_score]
close_scores = [close_score for _, close_score in scores if close_score]
      
answer = sum(error_scores)
print(answer)

import statistics

answer = statistics.median(close_scores)
print(answer)
