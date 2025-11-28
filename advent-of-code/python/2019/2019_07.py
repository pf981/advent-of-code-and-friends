from aocd import get_data

inp = get_data(day=7, year=2019)

import collections
import dataclasses
import enum
import itertools

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
    
  def __post_init__(self):
    self.instructions = self.instructions.copy()
    
  def get_param(self, param_number, mode):
    index = self.instructions[self.i + param_number + 1]
    if mode == 0:
      pass
    elif mode == 1:
      self.instructions[str(index)] = index
      index = str(index)
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
    elif op_code == 99:
      self.state = State.HALTED
    else:
      raise ValueError(f'Invalid op code: {op_code} at position {self.i}')

    return self.state

def compute_thruster_output(instructions, phases):
  amplifiers = [Computer(instructions, [phase]) for phase in phases]
  output = [0]
  
  for amplifier in amplifiers:
    amplifier.input_values.extend(output)
    
    while amplifier.run_once() == State.READY:
      pass
    output = amplifier.output_values

  return output[0]

instructions = collections.defaultdict(int, {i: int(x) for i, x in enumerate(inp.split(','))})

answer = max(compute_thruster_output(instructions, phases) for phases in itertools.permutations(range(5)))
print(answer)

def compute_thruster_output2(instructions, phases):
  amplifiers = [Computer(instructions, [phase]) for phase in phases]
  output = [0]
  
  while amplifiers[-1].state != State.HALTED:
    for amplifier in amplifiers:
      amplifier.input_values.extend(output)

      while amplifier.run_once() == State.READY:
        pass
      output = amplifier.output_values.copy()
      amplifier.output_values.clear()

  return output[0]

answer = max(compute_thruster_output2(instructions, phases) for phases in itertools.permutations(range(5, 10)))
print(answer)
