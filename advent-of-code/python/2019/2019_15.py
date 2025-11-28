from aocd import get_data

inp = get_data(day=15, year=2019)

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
  
  def __lt__(self, other):
    return True # Need order defined, but don't care about implementation

import copy
import heapq

def create_area_map(instructions):
  states = [(0, 0, 0, Computer(instructions))]
  area_map = set()
  d_to_oxygen = oxygen_x = oxygen_y = None
  
  while states:
    d, x, y, bot = heapq.heappop(states)
    
    if (x, y) in area_map:
      continue
    area_map.add((x, y))
    
    for direction in range(1, 5):
      new_x = x + (direction == 4) - (direction == 3)
      new_y = y + (direction == 2) - (direction == 1)
      
      new_bot = copy.deepcopy(bot)
      new_bot.input_values.append(direction)
      output = new_bot.run().output_values.pop()
      
      if output == 0: # Wall
        continue
      elif output == 1: # Move
        heapq.heappush(states, (d + 1, new_x, new_y, new_bot))
      elif output == 2: # Oxygen system
        d_to_oxygen = d_to_oxygen or d + 1
        oxygen_x = oxygen_x or x
        oxygen_y = oxygen_y or y

  return d_to_oxygen, oxygen_x, oxygen_y, area_map


instructions = collections.defaultdict(int, {i: int(x) for i, x in enumerate(inp.split(','))})

d_to_oxygen, oxygen_x, oxygen_y, area_map = create_area_map(instructions)

answer = d_to_oxygen
print(answer)

def compute_oxygen_fill_time(area_map, oxygen_x, oxygen_y):
  states = [(0, oxygen_x, oxygen_y)]
  visited = set()
  max_d = 0
  
  while states:
    d, x, y = heapq.heappop(states)
    
    if (x, y) in visited:
      continue
    visited.add((x, y))
      
    max_d = max(max_d, d)
    
    for direction in range(1, 5):
      new_x = x + (direction == 4) - (direction == 3)
      new_y = y + (direction == 2) - (direction == 1)
      
      if (new_x, new_y) in area_map:
        heapq.heappush(states, (d + 1, new_x, new_y))
  
  return max_d + 1


answer = compute_oxygen_fill_time(area_map, oxygen_x, oxygen_y)
print(answer)
