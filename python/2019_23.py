from aocd import get_data

inp = get_data(day=23, year=2019)

import collections
import dataclasses
import enum

class State(enum.Enum):
  READY = enum.auto()
  WAITING_FOR_INPUT = enum.auto()
  HALTED = enum.auto()

@dataclasses.dataclass
class Computer:
  instructions: collections.defaultdict
  input_values: list = dataclasses.field(default_factory=list)
  output_values: list = dataclasses.field(default_factory=list)
  i: int = 0
  state: State = State.READY
  relative_base: int = 0
  idle: bool = False
    
  def __post_init__(self):
    self.instructions = self.instructions.copy()
    
  def get_param(self, param_number, mode):
    index = self.instructions[self.i + param_number + 1]
    if mode == 0:
      pass
    elif mode == 1:
      self.instructions[str(index)] = index
      index = str(index)
    elif mode == 2:
      index += self.relative_base
    return index
  
  def get_params(self):
    m3, m2, m1, *opcode = str(self.instructions[self.i]).zfill(5)
    p1, p2, p3 = (self.get_param(param_number, int(mode)) for param_number, mode in enumerate([m1, m2, m3]))
    return p1, p2, p3, int(''.join(opcode))
  
  def run_once(self):
    self.state = State.READY
    p1, p2, p3, op_code = self.get_params()

    if op_code == 1:
      self.instructions[p3] = self.instructions[p1] + self.instructions[p2]
      self.i += 4
    elif op_code == 2:
      self.instructions[p3] = self.instructions[p1] * self.instructions[p2]
      self.i += 4
    elif op_code == 3:
      if self.input_values:
        self.instructions[p1] = self.input_values.pop(0)
        self.i += 2
      else:
        self.idle = True
        self.instructions[p1] = -1
        self.i += 2
    elif op_code == 4:
      self.output_values.append(self.instructions[p1])
      self.i += 2
    elif op_code == 5:
      if self.instructions[p1] != 0:
        self.i = self.instructions[p2]
      else:
        self.i += 3
    elif op_code == 6:
      if self.instructions[p1] == 0:
        self.i = self.instructions[p2]
      else:
        self.i += 3
    elif op_code == 7:
      self.instructions[p3] = self.instructions[p1] < self.instructions[p2]
      self.i += 4
    elif op_code == 8:
      self.instructions[p3] = self.instructions[p1] == self.instructions[p2]
      self.i += 4
    elif op_code == 9:
      self.relative_base += self.instructions[p1]
      self.i += 2
    elif op_code == 99:
      self.state = State.HALTED
    else:
      raise ValueError(f'Invalid op code: {op_code} at position {self.i}')

    return self
  
  def run(self):
    while self.run_once().state == State.READY:
      pass
    return self
  
  def run_n(self, n):
    self.idle = False
    for _ in range(n):
      self.run_once()
    return self

instructions = collections.defaultdict(int, {i: int(x) for i, x in enumerate(inp.split(','))})

def solve(instructions):
  bots = [Computer(instructions, [i]) for i in range(50)]

  while True:
    for bot in bots:
      output = bot.run_n(100).output_values
      while len(output) > 2:
        destination, x, y = output.pop(0), output.pop(0), output.pop(0)
        if destination == 255:
          return y
        bots[destination].input_values.extend([x, y])

answer = solve(instructions)
print(answer)

def solve2(instructions):
  bots = [Computer(instructions, [i]) for i in range(50)]
  nat = None
  last_y = None
  idle_count = 0
  
  while True:
    for bot in bots:
      output = bot.run_n(100).output_values
      while len(output) > 2:
        destination, x, y = output.pop(0), output.pop(0), output.pop(0)
        if destination == 255:
          nat = x, y
        else:
          bots[destination].input_values.extend([x, y])
      if not bot.idle:
        idle_count = 0

    idle_count += 1
    if idle_count >= 3:
      idle_count = 0
      if nat[1] == last_y:
        return last_y
      last_y = nat[1]
      bots[0].input_values.extend(nat)

answer = solve2(instructions)
print(answer)
