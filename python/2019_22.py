from aocd import get_data

inp = get_data(day=22, year=2019)

import re

def get_shuffle_coefficients(instructions, n_cards):
  a, b = 1, 0
  for line in instructions.splitlines():
    if line.startswith('deal into'):
      a = a * -1 % n_cards
      b = (n_cards - 1 - b) % n_cards
    elif line.startswith('deal with'):
      increment = int(re.findall(r'-?\d+', line)[0])
      a = a * increment % n_cards
      b = b * increment % n_cards
    else:
      cut = int(re.findall(r'-?\d+', line)[0])
      b = (b - cut) % n_cards
  
  return a, b

def solve(instructions, n_cards, n_shuffles, target):
  # Find a and b such that
  #     position_after_shuffle = a * position_before_shuffle + b MOD n
  a, b = get_shuffle_coefficients(instructions, n_cards)

  # Let A and B be the coefficients after 101741582076661 applications of a*x + b

  # We have
  #     a*x + b
  # Which after one iteration, goes to
  #     a*(a*x + b) + b = a^2*x + b + b*a
  # After two iterations
  #    a^2*(a*x + b) + b + ab = a^3*x + b + b*a + b*a^2
  # After n iterations
  #    a^n*x + b + b*a + b*a^2 + ... + b*a^(n-1) = A*x + B where
  #    A = a^n, and
  #    B = sum of i from 0 to n-1 of b*a^i
  #
  # B is a geometric series which can be evaluated as
  #    B = b * (a^n - 1) * (a - 1)' = b*(A-1)*(a-1)'
  A = pow(a, n_shuffles, n_cards)
  B = b * (A - 1) * pow(a - 1, n_cards - 2, n_cards) % n_cards

  position_of_target_card = (A * target + B) % n_cards
  
  # We need to find x such that
  #      A*x + B = 2020          MOD n
  #   =>       x = A'*(2020 - B) MOD n
  card_at_target_position = pow(A, n_cards - 2, n_cards) * (target - B) % n_cards
  
  return position_of_target_card, card_at_target_position

answer = solve(inp, 10007, 1, 2019)[0]
print(answer)

answer = solve(inp, 119315717514047, 101741582076661, 2020)[1]
print(answer)
