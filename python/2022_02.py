from aocd import get_data

inp = get_data(day=2, year=2022)

names = {
  'A': 'Rock',
  'B': 'Paper',
  'C': 'Scissors',
  'X': 'Rock',
  'Y': 'Paper',
  'Z': 'Scissors'
}

result_score = {
  ('Rock', 'Rock'): 3,
  ('Rock', 'Paper'): 6,
  ('Rock', 'Scissors'): 0,
  ('Paper', 'Rock'): 0,
  ('Paper', 'Paper'): 3,
  ('Paper', 'Scissors'): 6,
  ('Scissors', 'Rock'): 6,
  ('Scissors', 'Paper'): 0,
  ('Scissors', 'Scissors'): 3
}

shape_score = {
  'Rock': 1,
  'Paper': 2,
  'Scissors': 3
}

strategy = [[names[c] for c in line.split(' ')] for line in inp.splitlines()]
score = sum(shape_score[b] + result_score[(a, b)] for a, b in strategy)
answer = score
print(answer)

results = {
  'Rock': 'Lose',
  'Paper': 'Draw',
  'Scissors': 'Win'
}

force_result = {
  ('Rock', 'Lose'): 'Scissors',
  ('Rock', 'Draw'): 'Rock',
  ('Rock', 'Win'): 'Paper',
  ('Paper', 'Lose'): 'Rock',
  ('Paper', 'Draw'): 'Paper',
  ('Paper', 'Win'): 'Scissors',
  ('Scissors', 'Lose'): 'Paper',
  ('Scissors', 'Draw'): 'Scissors',
  ('Scissors', 'Win'): 'Rock'
}

score = 0
for a, result in strategy:
  result = results[result]
  b = force_result[(a, result)]
  score += shape_score[b] + result_score[(a, b)]

answer = score
print(answer)
