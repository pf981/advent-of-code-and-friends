# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/19

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 19: Tractor Beam ---</h2><p>Unsure of the state of Santa's ship, you <span title="&quot;borrowed&quot;">borrowed</span> the tractor beam technology from Triton. Time to test it out.</p>
# MAGIC <p>When you're safely away from anything else, you activate the tractor beam, but nothing happens.  It's hard to tell whether it's working if there's nothing to use it on. Fortunately, your ship's drone system can be configured to deploy a drone to specific coordinates and then check whether it's being pulled. There's even an <a href="9">Intcode</a> program (your puzzle input) that gives you access to the drone system.</p>
# MAGIC <p>The program uses two input instructions to request the <em>X and Y position</em> to which the drone should be deployed.  Negative numbers are invalid and will confuse the drone; all numbers should be <em>zero or positive</em>.</p>
# MAGIC <p>Then, the program will output whether the drone is <em>stationary</em> (<code>0</code>) or <em>being pulled by something</em> (<code>1</code>). For example, the coordinate X=<code>0</code>, Y=<code>0</code> is directly in front of the tractor beam emitter, so the drone control program will always report <code>1</code> at that location.</p>
# MAGIC <p>To better understand the tractor beam, it is important to <em>get a good picture</em> of the beam itself. For example, suppose you scan the 10x10 grid of points closest to the emitter:</p>
# MAGIC <pre><code>       X
# MAGIC   0-&gt;      9
# MAGIC  0#.........
# MAGIC  |.#........
# MAGIC  v..##......
# MAGIC   ...###....
# MAGIC   ....###...
# MAGIC Y .....####.
# MAGIC   ......####
# MAGIC   ......####
# MAGIC   .......###
# MAGIC  9........##
# MAGIC </code></pre>
# MAGIC <p>In this example, the <em>number of points affected by the tractor beam</em> in the 10x10 area closest to the emitter is <code><em>27</em></code>.</p>
# MAGIC <p>However, you'll need to scan a larger area to <em>understand the shape</em> of the beam. <em>How many points are affected by the tractor beam in the 50x50 area closest to the emitter?</em> (For each of X and Y, this will be <code>0</code> through <code>49</code>.)</p>
# MAGIC </article>

# COMMAND ----------

inp = '109,424,203,1,21102,11,1,0,1105,1,282,21102,18,1,0,1105,1,259,1201,1,0,221,203,1,21101,31,0,0,1105,1,282,21101,38,0,0,1106,0,259,21002,23,1,2,22101,0,1,3,21102,1,1,1,21101,0,57,0,1105,1,303,1201,1,0,222,20102,1,221,3,21001,221,0,2,21101,259,0,1,21101,0,80,0,1105,1,225,21102,1,76,2,21101,91,0,0,1106,0,303,1201,1,0,223,21001,222,0,4,21102,1,259,3,21101,0,225,2,21102,1,225,1,21102,1,118,0,1106,0,225,20101,0,222,3,21101,100,0,2,21102,1,133,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21101,148,0,0,1105,1,259,2102,1,1,223,20102,1,221,4,21001,222,0,3,21101,0,17,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,0,195,0,106,0,109,20207,1,223,2,21002,23,1,1,21102,1,-1,3,21101,214,0,0,1105,1,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,1201,-4,0,249,22101,0,-3,1,21201,-2,0,2,22102,1,-1,3,21101,0,250,0,1106,0,225,22101,0,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2105,1,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2105,1,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22101,0,-2,3,21102,1,343,0,1105,1,303,1106,0,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21102,1,384,0,1106,0,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21201,1,0,-4,109,-5,2106,0,0'

# COMMAND ----------

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

instructions = collections.defaultdict(int, {i: int(x) for i, x in enumerate(inp.split(','))})

# COMMAND ----------

def check(row, col):
  return Computer(instructions, [row, col]).run().output_values[0]

def solve(instructions):
  result = 0
  for row in range(50):
    for col in range(50):
      if check(row, col):
        result += 1
  return result

answer = solve(instructions)
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You aren't sure how large Santa's ship is. You aren't even sure if you'll need to use this thing on Santa's ship, but it doesn't hurt to be prepared. You figure Santa's ship might fit in a <em>100x100</em> square.</p>
# MAGIC <p>The beam gets wider as it travels away from the emitter; you'll need to be a minimum distance away to fit a square of that size into the beam fully. (Don't rotate the square; it should be aligned to the same axes as the drone grid.)</p>
# MAGIC <p>For example, suppose you have the following tractor beam readings:</p>
# MAGIC <pre><code>#.......................................
# MAGIC .#......................................
# MAGIC ..##....................................
# MAGIC ...###..................................
# MAGIC ....###.................................
# MAGIC .....####...............................
# MAGIC ......#####.............................
# MAGIC ......######............................
# MAGIC .......#######..........................
# MAGIC ........########........................
# MAGIC .........#########......................
# MAGIC ..........#########.....................
# MAGIC ...........##########...................
# MAGIC ...........############.................
# MAGIC ............############................
# MAGIC .............#############..............
# MAGIC ..............##############............
# MAGIC ...............###############..........
# MAGIC ................###############.........
# MAGIC ................#################.......
# MAGIC .................########<em>O</em>OOOOOOOOO.....
# MAGIC ..................#######OOOOOOOOOO#....
# MAGIC ...................######OOOOOOOOOO###..
# MAGIC ....................#####OOOOOOOOOO#####
# MAGIC .....................####OOOOOOOOOO#####
# MAGIC .....................####OOOOOOOOOO#####
# MAGIC ......................###OOOOOOOOOO#####
# MAGIC .......................##OOOOOOOOOO#####
# MAGIC ........................#OOOOOOOOOO#####
# MAGIC .........................OOOOOOOOOO#####
# MAGIC ..........................##############
# MAGIC ..........................##############
# MAGIC ...........................#############
# MAGIC ............................############
# MAGIC .............................###########
# MAGIC </code></pre>
# MAGIC <p>In this example, the <em>10x10</em> square closest to the emitter that fits entirely within the tractor beam has been marked <code>O</code>. Within it, the point closest to the emitter (the only highlighted <code><em>O</em></code>) is at X=<code>25</code>, Y=<code>20</code>.</p>
# MAGIC <p>Find the <em>100x100</em> square closest to the emitter that fits entirely within the tractor beam; within that square, find the point closest to the emitter.  <em>What value do you get if you take that point's X coordinate, multiply it by <code>10000</code>, then add the point's Y coordinate?</em> (In the example above, this would be <code>250020</code>.)</p>
# MAGIC </article>

# COMMAND ----------

import itertools

def solve2(instructions):
  x_right = 5
  for y in itertools.count(4):
    y_bottom = y + 99
    
    while check(x_right + 1, y):
      x_right += 1
    x = x_right - 99

    if check(x_right, y) and check(x, y_bottom):
      return 10000 * x + y

answer = solve2(instructions)
print(answer)
