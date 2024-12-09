from aocd import get_data

inp = get_data(day=25, year=2019)

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
  
  def go(self, command, do_print=True):
    if command:
      self.input_values.extend(ord(c) for c in command + '\n')
    self.run()
    
    if do_print:
      if command:
        print(f'$ {command}')
      print(''.join(chr(x) for x in self.output_values))
      self.output_values.clear()
    
    return self

instructions = collections.defaultdict(int, {i: int(x) for i, x in enumerate(inp.split(','))})
computer = Computer(instructions)
computer.go('')
computer.go('west')
computer.go('west')
computer.go('take loom')
computer.go('east')
computer.go('east')
computer.go('north')
computer.go('north')
computer.go('take mutex')
computer.go('east')
computer.go('take tambourine')
computer.go('west')
computer.go('south')
computer.go('west')
computer.go('take antenna')
computer.go('south')
computer.go('take hologram')
computer.go('south')
computer.go('take mug')
computer.go('north')
computer.go('west')
computer.go('take astronaut ice cream')
computer.go('east')
computer.go('north')
computer.go('north')
computer.go('north')
computer.go('north')
computer.go('take space heater')
computer.go('north')
computer.go('east')
computer.go('drop mutex')
computer.go('drop loom')
computer.go('drop tambourine')
computer.go('drop mug')
computer.go('east')

answer = 25166400
print(answer)

# No puzzle here - just need 49 stars.
