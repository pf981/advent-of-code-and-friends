from aocd import get_data

inp = get_data(day=5, year=2019)

import collections
import dataclasses

@dataclasses.dataclass
class Computer:
  instructions: collections.defaultdict
  input_value: int = 1
  i: int = 0
    
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
  
  def run(self):
    while True:
      p1, p2, p3, op_code = self.get_params()
      
      if op_code == 1:
        self.instructions[p3] = self.instructions[p1] + self.instructions[p2]
        self.i += 4
      elif op_code == 2:
        self.instructions[p3] = self.instructions[p1] * self.instructions[p2]
        self.i += 4
      elif op_code == 3:
        self.instructions[p1] = self.input_value
        self.i += 2
      elif op_code == 4:
        self.input_value = self.instructions[p1]
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
        break
      else:
        raise ValueError(f'Invalid op code: {op_code} at position {self.i}')

    return self.input_value

instructions = collections.defaultdict(int, {i: int(x) for i, x in enumerate(inp.split(','))})

answer = Computer(instructions, 1).run()
print(answer)

answer = Computer(instructions, 5).run()
print(answer)
