from aocd import get_data

inp = get_data(day=17, year=2019)

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
        self.state = State.WAITING_FOR_INPUT
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

def get_alignment_parameters_sum(scaffold):
  alignment_parameters_sum = 0
  for row, col in scaffold:
    neighbors = sum((row + dr, col + dc) in scaffold for dr, dc in ((0, -1), (0, 1), (-1, 0), (1, 0)))
    if neighbors == 4:
      alignment_parameters_sum += row * col
  return alignment_parameters_sum


instructions = collections.defaultdict(int, {i: int(x) for i, x in enumerate(inp.split(','))})

output = ''.join(chr(x) for x in Computer(instructions).run().output_values)
values = [(row, col, value) for col, line in enumerate(output.splitlines()) for row, value in enumerate(line)]
scaffold = {(row, col) for row, col, value in values if value != '.'}
start = {(row, col, value) for row, col, value in values if value not in '.#'}

answer = get_alignment_parameters_sum(scaffold)
print(answer)

input_sequence_str = '''A,B,A,B,C,B,C,A,C,C
R,12,L,10,L,10
L,6,L,12,R,12,L,4
L,12,R,12,L,6
n
'''

instructions[0] = 2
answer = Computer(instructions, [ord(x) for x in input_sequence_str]).run().output_values[-1]
print(answer)
