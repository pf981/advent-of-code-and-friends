from aocd import get_data, submit
import math
import re


def parse_part(part):
  if ':' not in part:
    return (part, )
  rule, destination = part.split(':')
  c, op, val = re.match(r'([xmas])([<>])([0-9]+)', rule).groups()
  return (c, op, int(val)), destination


def parse_workflow(line):
  name, parts = re.match(r'([a-z]+){(.+)}', line).groups()
  return name, [parse_part(part) for part in parts.split(',')]


def resolve(machine_part, workflow_name, workflows):
  if workflow_name in 'AR':
    return workflow_name
  for part in workflows[workflow_name]:
    if len(part) == 1:
      return resolve(machine_part, part[0], workflows)

    (c, op, val), destination = part
    if eval(f'{machine_part[c]} {op} {val}'):
      return resolve(machine_part, destination, workflows)


inp = get_data(day=19, year=2023)
workflows, machine_parts = inp.split('\n\n')
workflows = dict([parse_workflow(workflow) for workflow in workflows.splitlines()])
machine_parts = [dict(zip('xmas', [int(num) for num in re.findall(r'\d+', machine_part)])) for machine_part in machine_parts.splitlines()]

answer1 = sum(sum(machine_part.values()) for machine_part in machine_parts if resolve(machine_part, 'in', workflows) == 'A')
print(answer1)

submit(answer1, part='a', day=19, year=2023)


# Part 2


def count_solutions(ranges, workflow_name, workflows):
  if any(end <= start for start, end in ranges.values()):
    return 0
  if workflow_name == 'A':
    return math.prod(end - start for start, end in ranges.values())
  if workflow_name == 'R':
    return 0

  n_solutions = 0
  for part in workflows[workflow_name]:
    if len(part) == 1:
      n_solutions += count_solutions(ranges, part[0], workflows)
      break

    c, op, val = part[0]
    next_workflow_name = part[1]
    new_ranges = ranges.copy()

    if op == '<':
      if ranges[c][0] < val <= ranges[c][1]:
        new_ranges[c] = (new_ranges[c][0], val)
        n_solutions += count_solutions(new_ranges, next_workflow_name, workflows)
        ranges[c] = (val, ranges[c][1])
    if op == '>':
      if ranges[c][0] <= val < ranges[c][1]:
        new_ranges[c] = (val + 1, new_ranges[c][1])
        n_solutions += count_solutions(new_ranges, next_workflow_name, workflows)
        ranges[c] = (ranges[c][0], val + 1)

  return n_solutions


answer2 = count_solutions(dict(zip('xmas', [(1, 4001)] * 4)), 'in', workflows)
print(answer2)

submit(answer2, part='b', day=19, year=2023)
