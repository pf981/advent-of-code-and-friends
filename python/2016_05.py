from aocd import get_data

inp = get_data(day=5, year=2016)

from hashlib import md5
from itertools import count

answer = ''
for i in count():
  result = md5((inp + str(i)).encode()).hexdigest()
  if result.startswith('0' * 5):
    answer += result[5]
    if len(answer) == 8:
      break
answer

answer = [None] * 8
for i in count():
  result = md5((inp + str(i)).encode()).hexdigest()
  if result.startswith('0' * 5):
    try:
      j = int(result[5])
      if answer[j] is None:
        answer[j] = result[6]
        if all(c is not None for c in answer):
          break
    except (IndexError, ValueError):
      pass

answer = ''.join(answer)
answer
