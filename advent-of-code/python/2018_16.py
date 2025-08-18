from aocd import get_data

inp = get_data(day=16, year=2018)

import re

all_ops = ('addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr')

def execute(op, a, b, c, r):
  if op in ('addi', 'addr', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'gtri', 'gtrr', 'eqri', 'eqrr'):
    a = r[a]
  if op in ('addr', 'mulr', 'banr', 'borr', 'gtir', 'gtrr', 'eqir', 'eqrr'):
    b = r[b]
  
  if op.startswith('add'):
    r[c] = a + b
  elif op.startswith('mul'):
    r[c] = a * b
  elif op.startswith('ban'):
    r[c] = a & b
  elif op.startswith('bor'):
    r[c] = a | b
  elif op.startswith('set'):
    r[c] = a
  elif op.startswith('gt'):
    r[c] = int(a > b)
  elif op.startswith('eq'):
    r[c] = int(a == b)

def get_possible_ops(before, instruction, after):
  possible_ops = set()
  _, a, b, c = instruction
  for op in all_ops:
    r = before.copy()
    execute(op, a, b, c, r)
    if r == after:
      possible_ops.add(op)
  return possible_ops

effects, instructions = inp.split('\n\n\n\n')
effects = [[[int(x) for x in group] for group in re.findall(r'(\d+),? (\d+),? (\d+),? (\d+)', line)] for line in effects.split('\n\n')]
instructions = [[int(x) for x in line.split(' ')] for line in instructions.splitlines()]

possible_ops = [get_possible_ops(before, instruction, after) for before, instruction, after in effects]

answer = sum(len(x) >= 3 for x in possible_ops)
print(answer)

import collections

def get_mapping(possible_mapping, op_mapping):
  if len(op_mapping) == 16:
    return op_mapping
  
  opcode, ops = min(possible_mapping.items(), key=lambda x: len(x[1]))

  for op in ops:
    if op in op_mapping.values():
      continue

    new_possible_mapping = possible_mapping.copy()
    del new_possible_mapping[opcode]
    
    new_op_mapping = op_mapping.copy()
    new_op_mapping[opcode] = op
    
    result = get_mapping(new_possible_mapping, new_op_mapping)
    if result:
      return result
  return None


def solve(effects):
  possible_mapping = collections.defaultdict(lambda: set(all_ops))
  for opcode, ops in zip([op for _, (op, _, _, _), _ in effects], possible_ops):
    possible_mapping[opcode] &= ops

  mapping = get_mapping(possible_mapping, {})

  r = [0] * 4
  for opcode, a, b, c in instructions:
    execute(mapping[opcode], a, b, c, r)
  
  return r[0]

answer = solve(effects)
print(answer)
