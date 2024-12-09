from aocd import get_data

inp = get_data(day=20, year=2016)

def solve(ends, max_allowed = 4294967295):
  i = 0
  count_allowed = 0
  first_allowed = None
  
  while i <= max_allowed:
    new_end = max(end for start, end in ends if start <= i)
    if new_end <= i:
      first_allowed = first_allowed or i
      new_end = min((start for start, end in ends if start > i), default=max_allowed)
      count_allowed += new_end - i
    i = new_end + 1
  
  return first_allowed, count_allowed

first_allowed, count_allowed = solve([[int(x) for x in line.split('-')] for line in inp.split('\n')])

answer = first_allowed
answer

answer = count_allowed
answer
