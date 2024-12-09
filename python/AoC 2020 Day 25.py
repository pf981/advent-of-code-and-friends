from aocd import get_data

inp = get_data(day=25, year=2020)

import itertools


def transform(subject_number, loop_size):
  value = 1
  for _ in range(loop_size):
    value *= subject_number
    value %= 20201227
  return value


def get_loop_size(public_key):
  value = 1
  for loop_size in itertools.count():
    if value == public_key:
      return loop_size
    value *= 7
    value %= 20201227


card_public_key, door_public_key = (int(x) for x in inp.splitlines())
card_loop_size = get_loop_size(card_public_key)
encryption_key = transform(door_public_key, card_loop_size)
answer = encryption_key
print(answer)

# No puzzle here - just need 49 stars.
