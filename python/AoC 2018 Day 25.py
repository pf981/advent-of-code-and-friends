from aocd import get_data

inp = get_data(day=25, year=2018)

def in_range(p1, p2):
  return sum(abs(x1 - x2) for x1, x2 in zip(p1, p2)) <= 3

points = tuple(tuple(int(x) for x in line.split(',')) for line in inp.splitlines())

group_members = [{p2 for p2 in points if in_range(p1, p2)} for p1 in points]
groups = [i for i, _ in enumerate(group_members)]

for group, members in enumerate(group_members):
  groups_to_merge = set()
  for i, merge_members in enumerate(group_members):
    if members & merge_members:
      groups_to_merge.add(groups[i])

  for i, group2 in enumerate(groups):
    if group2 in groups_to_merge:
      groups[i] = group

answer = len(set(groups))
print(answer)

# No puzzle here - just need 49 stars.
