from aocd import get_data

inp = get_data(day=24, year=2021)

import functools

ops = [line.split(' ') for line in inp.splitlines()]


def run(step, input_z, digit):
  input_i = 0
  r = {
    'w': digit,
    'x': 0,
    'y': 0,
    'z': input_z,
  }
  for i in range(18 * step + 1, 18 * (step + 1)):
    op, *args = ops[i]
    arg_values = [r[arg] if arg in r else int(arg) for arg in args]

    if op == 'add':
      r[args[0]] += arg_values[1]
    elif op == 'mul':
      r[args[0]] *= arg_values[1]
    elif op == 'div':
      r[args[0]] //= arg_values[1]
    elif op == 'mod':
      r[args[0]] %= arg_values[1]
    elif op == 'eql':
      r[args[0]] = int(arg_values[0] == arg_values[1])

  return r['z']


@functools.lru_cache(maxsize=None)
def solve(step, input_z, find_min):
  if step == 14:
    return '' if input_z == 0 else None
  
  digit_order = range(1, 10) if find_min else range(9, -1, -1)
    
  for digit in digit_order:
    output_z = run(step, input_z, digit)
    other_digits = solve(step + 1, output_z, find_min)

    if other_digits is not None:
      return str(digit) + other_digits
    

solve.cache_clear()

answer = solve(0, 0, False) # 1.5 hrs
print(answer)

answer = solve(0, 0, True) # 1 minute
print(answer)
