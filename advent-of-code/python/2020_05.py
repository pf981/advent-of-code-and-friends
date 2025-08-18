from aocd import get_data

inp = get_data(day=5, year=2020)

ids = set()
for seat in inp.split():
  row = int(''.join(str(int(c == 'B')) for c in seat[:7]), 2)
  col = int(''.join(str(int(c == 'R')) for c in seat[7:]), 2)
  ids.add(row * 8 + col)

answer = max(ids)
print(answer)

for seat in range(max(ids)):
  if seat not in ids and seat - 1 in ids and seat + 1 in ids:
    print(seat)
