from aocd import get_data

inp = get_data(day=18, year=2017)

import collections
import dataclasses
import typing

@dataclasses.dataclass
class Computer:
  program_id: int
  instructions: dict
  i: int = 0
  registers: typing.DefaultDict[str, int] = dataclasses.field(init=False)
  signal_out: list =  dataclasses.field(default_factory=lambda: [])
  send_count: int = 0
    
  def __post_init__(self):
    self.registers = collections.defaultdict(int, {'p': self.program_id})
  
  def get(self, x):
    try:
      return int(x)
    except ValueError:
      return self.registers[x]
  
  def run(self, signal_in):
    if self.i >= len(self.instructions):
      return False
    op, *args = self.instructions[self.i]
    a, b, *_ = args + [None]
    v_a, v_b, *_ = [self.get(x) for x in args] + [None]

    if op == 'snd':
      self.signal_out.append(v_a)
      self.send_count += 1
    elif op == 'set':
      self.registers[a] = v_b
    elif op == 'add':
      self.registers[a] += v_b
    elif op == 'mul':
      self.registers[a] *= v_b
    elif op == 'mod':
      self.registers[a] %= v_b
    elif op == 'rcv':
      if signal_in:
        self.registers[a] = signal_in.pop(0)
      else:
        return False
    elif op == 'jgz':
      if v_a > 0:
        self.i += v_b - 1
    self.i += 1
    return True


instructions = {i: line.split(' ') for i, line in enumerate(inp.split('\n'))}
    
computer = Computer(0, instructions)
while computer.run(None):
  pass

answer = computer.signal_out[-1]
print(answer)

c0 = Computer(0, instructions)
c1 = Computer(1, instructions)
while c0.run(c1.signal_out) or c1.run(c0.signal_out):
  pass

answer = c1.send_count
print(answer)
