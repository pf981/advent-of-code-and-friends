from aocd import get_data

inp = get_data(day=23, year=2016)

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
    
    if instruction == 'cpy':
      try:
        int(args[1])
      except ValueError:
        self.registers[args[1]] = self._get_value(args[0])
    elif instruction == 'inc':
      self.registers[args[0]] += 1
    elif instruction == 'dec':
      self.registers[args[0]] -= 1
    elif instruction == 'jnz':
      if self._get_value(args[0]) != 0:
        self.line_number += self._get_value(args[1]) - 1
    elif instruction == 'tgl':
      target_line = self.line_number + self._get_value(args[0])
      if target_line < len(self.instructions):
        self.instructions[target_line][0] = {
          'cpy': 'jnz',
          'inc': 'dec',
          'dec': 'inc',
          'jnz': 'cpy',
          'tgl': 'inc'
        }[self.instructions[target_line][0]]
    elif instruction == 'mul':
      self.registers[args[2]] = self._get_value(args[0]) * self._get_value(args[1])
    elif instruction == 'nop':
      pass
    else:
      raise ValueError(f'Unknown instruction: {instruction}')
    
    self.line_number += 1
    if self.line_number >= len(self.instructions):
      self.status = 'Halted'
  
  def run(self):
    while self.status != 'Halted':
      self.run_once()


instructions = {i: [line.split()[0], tuple(line.split()[1:])] for i, line in enumerate(inp.split('\n'))}

computer = Computer(instructions)
computer.registers['a'] = 7
computer.run()

answer = computer.registers['a']
answer

# Label |  Line  |  Instruction  |    V1                |    V2                            |  V3
# -----------------------------------------------------------------------------------------|-------------
#       |  0     |  cpy a b      |    b = a             |                                  |             
#       |  1     |  dec b        |    b--               |                                  |             
# D:    |  2     |  cpy a d      |    d = a             |                                  |             
#       |  3     |  cpy 0 a      |    a = 0             |                                  |             
# B:    |  4     |  cpy b c      |    c = b             |  WHILE d > 0 { c = b             |  a = d * b  
# A:    |  5     |  inc a        |    a++               |                WHILE C > 0 { a++ |  ;          
#       |  6     |  dec c        |    c--               |                              c-- |  ;          
#       |  7     |  jnz c -2     |    IF c != 0 GOTO A  |                }                 |  ;          
#       |  8     |  dec d        |    d--               |                d--               |  ;          
#       |  9     |  jnz d -5     |    if d != 0 GOTO B  |              }                   |  ;          
#       |  10    |  dec b        |    b--               |  b--                             |  b--        
#       |  11    |  cpy b c      |    c = b             |                                  |             
#       |  12    |  cpy c d      |    d = c             |                                  |             
# C:    |  13    |  dec d        |    d--               |                                  |             
#       |  14    |  inc c        |    c++               |                                  |             
#       |  15    |  jnz d -2     |    if d != 0 GOTO C  |                                  |             
#       |  16    |  tgl c        |    ???               |                                  |             
#       |  17    |  cpy -16 c    |    c = -16           |                                  |             
#       |  18    |  jnz 1 c      |    GOTO D            |                                  |             
#       |  19    |  cpy 95 c     |    c = 95            |                                  |             
# F:    |  20    |  jnz 99 d     |    GOTO d ???        |                                  |             
# E:    |  21    |  inc a        |    a--               |                                  |             
#       |  22    |  inc d        |    d--               |                                  |             
#       |  23    |  jnz d -2     |    IF d != 0 GOTO E  |                                  |             
#       |  24    |  inc c        |    c++               |                                  |             
#       |  25    |  jnz c -5     |    IF c != 0 GOTO F  |                                  |               

instructions[4] = ['mul', ('d', 'b', 'a')]
for i in range(5, 10):
  instructions[i] = ['nop', tuple()]

computer = Computer(instructions)
computer.registers['a'] = 12
computer.run()

answer = computer.registers['a']
answer
