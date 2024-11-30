from aocd import get_data, submit
import collections


inp = get_data(day=21, year=2023)
lines = inp.splitlines()
plots = {(row, col) for row, line in enumerate(lines) for col, c in enumerate(line) if c in 'S.'}
start_pos = next((row, col) for row, line in enumerate(lines) for col, c in enumerate(line) if c == 'S')

side_len = len(lines) # Assume square
target = 26501365
remainder = target % side_len

q = collections.deque([(start_pos, 0)])
seen = set() # (steps % 2, pos)

cur_step = 0
reach_counts = []
while q:
  pos, steps = q.popleft()

  if steps > cur_step:
    if cur_step == 64:
      answer1 = len({pos for i, pos in seen if i == cur_step % 2})
    if cur_step % side_len == remainder:
      reach_counts.append(len({pos for i, pos in seen if i == cur_step % 2}))
    cur_step = steps

  if (pos[0] % side_len, pos[1] % side_len) not in plots or (steps % 2, pos) in seen:
    continue
  seen.add((steps % 2, pos))

  if len(reach_counts) == 3:
    break

  for d in 'NESW':
    new_pos = (
      pos[0] + (d == 'S') - (d == 'N'),
      pos[1] + (d == 'E') - (d == 'W')
    )
    q.append((new_pos, steps + 1))

print(answer1)

submit(answer1, part='a', day=21, year=2023)


# Part 2


import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


poly = PolynomialFeatures(degree=2)

X = np.array([0, 1, 2]).reshape(-1, 1)
Y = np.array(reach_counts).reshape(-1, 1)
X2 = np.array(target // side_len).reshape(1, -1)

model = LinearRegression()
model.fit(poly.fit_transform(X), Y)

answer2 = model.predict(poly.transform(X2))[0][0].astype(int)
print(answer2)

submit(answer2, part='b', day=21, year=2023)
