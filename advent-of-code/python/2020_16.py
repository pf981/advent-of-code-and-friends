from aocd import get_data

inp = get_data(day=16, year=2020)

bounds, your_ticket, nearby = inp.split('\n\n')

valid_fields = {}
for line in bounds.splitlines():
  name, right = line.split(': ')
  valid_fields[name] = set()
  for bound in right.split(' or '):
    min_bound, max_bound = bound.split('-')
    for num in range(int(min_bound), int(max_bound) + 1):
      valid_fields[name].add(num)

your_ticket = [int(x) for x in your_ticket.splitlines()[1].split(',')]
nearby = [[int(x) for x in line.split(',')] for line in nearby.splitlines()[1:]]

valid_values = set()
for s in valid_fields.values():
  valid_values.update(s)

answer = sum(num for ticket in nearby for num in ticket if num not in valid_values)
print(answer)

n = len(your_ticket)

possibilities = {i: set(valid_fields.keys()) for i in range(n)}
for ticket in nearby:
  if any(num not in valid_values for num in ticket):
    continue
  
  for i in range(n):
    for field in possibilities[i].copy():
      if ticket[i] not in valid_fields[field]:
        possibilities[i].remove(field)

confirmed = {}
while possibilities:
  for i, fields in possibilities.items():
    if len(fields) == 1:
      field = next(iter(fields))
      confirmed[i] = field
      del possibilities[i]
      for fields in possibilities.values():
        fields.discard(field)
      break

answer = 1
for i, field in confirmed.items():
  if field.startswith('departure'):
    answer *= your_ticket[i]

print(answer)
