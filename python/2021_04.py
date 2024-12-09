from aocd import get_data

inp = get_data(day=4, year=2021)

draws, *boards = inp.split('\n\n')
draws = [int(draw) for draw in draws.split(',')]
boards = [[[int(x) for x in line.split(' ') if x] for line in board.splitlines()] for board in boards]

import copy

def has_won(board):
  for row in board:
    if all(num == -1 for num in row):
      return True

  for col in zip(*board):
    if all(num == -1 for num in col):
      return True
  
  return False

def winning_score(draws, boards, nth_winner=1):
  draws = draws.copy()
  boards = copy.deepcopy(boards)
  completed_boards = set()

  for draw in draws:
    for board_id, board in enumerate(boards):
      if board_id in completed_boards:
        continue

      for line in board:
        for i, _ in enumerate(line):
          line[i] = -1 if line[i] == draw else line[i]

      if has_won(board):
        completed_boards.add(board_id)
        if len(completed_boards) == nth_winner:
          return draw * sum(num for row in board for num in row if num != -1)

answer = winning_score(draws, boards)
print(answer)

answer = winning_score(draws, boards, len(boards))
print(answer)
