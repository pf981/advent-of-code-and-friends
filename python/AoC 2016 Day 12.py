from aocd import get_data

inp = get_data(day=12, year=2016)

from collections import defaultdict
from dataclasses import dataclass, field
from typing import DefaultDict

@dataclass
class Computer:
  instructions: dict
  registers: DefaultDict[str, int] = field(default_factory=lambda: defaultdict(int))
  line_number: int = 0
  status: str = 'Pending'
    
  def __post_init__(self):
    self.instructions = self.instructions.copy()
    
  def _get_value(self, x):
    try:
      return int(x)
    except ValueError:
      return self.registers[x]
  
  def run_once(self):
    instruction, args = self.instructions[self.line_number]
    
    if instruction == 'cpy':
      self.registers[args[1]] = self._get_value(args[0])
    elif instruction == 'inc':
      self.registers[args[0]] += 1
    elif instruction == 'dec':
      self.registers[args[0]] -= 1
    elif instruction == 'jnz':
      if self._get_value(args[0]) != 0:
        self.line_number += self._get_value(args[1]) - 1
    
    self.line_number += 1
    if self.line_number >= len(self.instructions):
      self.status = 'Halted'
  
  def run(self):
    while self.status != 'Halted':
      self.run_once()


instructions = {i: (line.split()[0], tuple(line.split()[1:])) for i, line in enumerate(inp.split('\n'))}

computer = Computer(instructions)
computer.run()

answer = computer.registers['a']
answer

computer = Computer(instructions)
computer.registers['c'] = 1
computer.run()

answer = computer.registers['a']
answer
