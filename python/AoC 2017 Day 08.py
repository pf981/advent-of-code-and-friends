from aocd import get_data

inp = get_data(day=8, year=2017)

import collections

def solve(instructions):
  registers = collections.defaultdict(int)
  overall_max_value = float('-inf')

  for result_register, op, value, _, lhs, cmp, rhs in instructions:
    if eval(f"registers['{lhs}'] {cmp} {rhs}"):
      registers[result_register] += {'inc': 1, 'dec': -1}[op] * int(value)
      overall_max_value = max(overall_max_value, registers[result_register])

  return max(registers.values()), overall_max_value

instructions = [line.split(' ') for line in inp.split('\n')]
last_max_value, overall_max_value = solve(instructions)

answer = last_max_value
print(answer)

answer = overall_max_value
print(answer)
