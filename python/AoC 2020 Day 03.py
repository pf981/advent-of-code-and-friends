from aocd import get_data

inp = get_data(day=3, year=2020)

m = inp.splitlines()
n_rows = len(m)
n_cols = len(m[0])
n_trees = 0
col = 0
for row in range(n_rows):
  n_trees += (m[row][col % n_cols] == '#')
  col += 3
  
answer = n_trees
print(answer)

answer = 1
for dc, dr in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
  n_trees = 0
  row = 0
  col = 0
  while row < n_rows:
    n_trees += (m[row][col % n_cols] == '#')
    row += dr
    col += dc
  answer *= n_trees

print(answer)
