from aocd import get_data

inp = get_data(day=22, year=2020)

import collections


def get_score(players):
  return sum(multiplier * card for multiplier, card in enumerate(reversed(players[0] or players[1]), 1))


players_start = tuple(tuple(int(x) for x in player.splitlines()[1:]) for player in inp.split('\n\n'))

players = [collections.deque(player) for player in players_start]
while players[0] and players[1]:
  cards = [player.popleft() for player in players]
  players[cards[1] > cards[0]].extend(sorted(cards, reverse=True))

answer = get_score(players)
print(answer)

def get_round_winner(players):
  if all(len(cards) >= top for top, *cards in players):
    players = play_game((players[0][1:players[0][0] + 1], players[1][1:players[1][0] + 1]))
    return int(bool(players[1]))

  return players[1][0] > players[0][0]


def simulate_round(players):
  round_winner = get_round_winner(players)
  if round_winner == 0:
    return (players[0][1:] + (players[0][0], players[1][0]), players[1][1:])
  return (players[0][1:], players[1][1:] + (players[1][0], players[0][0]))


def play_game(players):
  seen = set()
  while players[0] and players[1]:
    if players in seen:
      return (players[0], tuple())
    seen.add(players)

    players = simulate_round(players)
  return players


players = play_game(players_start)

answer = get_score(players)
print(answer) # 4 seconds
