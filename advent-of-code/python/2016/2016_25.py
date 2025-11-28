from aocd import get_data

inp = get_data(day=25, year=2016)

from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass, field
from typing import DefaultDict

@dataclass
class Computer:
  instructions: dict
  registers: DefaultDict[str, int] = field(default_factory=lambda: defaultdict(int))
  line_number: int = 0
  status: str = 'Pending'
    
  def __post_init__(self):
    self.instructions = deepcopy(self.instructions)
    
  def _get_value(self, x):
    try:
      return int(x)
    except ValueError:
      return self.registers[x]
  
  def run_once(self):
    instruction, args = self.instructions[self.line_number]
    out = None
    
    if instruction == 'cpy':
      self.registers[args[1]] = self._get_value(args[0])
    elif instruction == 'inc':
      self.registers[args[0]] += 1
    elif instruction == 'dec':
      self.registers[args[0]] -= 1
    elif instruction == 'jnz':
      if self._get_value(args[0]) != 0:
        self.line_number += self._get_value(args[1]) - 1
    elif instruction == 'out':
      out = self._get_value(args[0])
    else:
      raise ValueError(f'Unknown instruction: {instruction}')
    
    self.line_number += 1
    if self.line_number >= len(self.instructions):
      self.status = 'Halted'
    return out
  
  def is_clock(self):
    clock_i = 0
    while clock_i < 100:
      out = self.run_once()
      if self.status == 'Halted':
        return False
      
      if out is not None:
        if clock_i % 2 != out:
          return False
        clock_i += 1
    return True

instructions = {i: (line.split()[0], tuple(line.split()[1:])) for i, line in enumerate(inp.split('\n'))}

import itertools

for a in itertools.count():
  computer = Computer(instructions)
  computer.registers['a'] = a
  if computer.is_clock():
     break

answer = a
answer

# No puzzle here - just need 49 stars.
