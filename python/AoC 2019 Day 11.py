# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/11

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 11: Space Police ---</h2><p>On the way to Jupiter, you're <a href="https://www.youtube.com/watch?v=KwY28rpyKDE">pulled over</a> by the <em>Space Police</em>.</p>
# MAGIC <p>"Attention, unmarked spacecraft! You are in violation of Space Law! All spacecraft must have a clearly visible <em>registration identifier</em>! You have 24 hours to comply or be sent to <a href="https://www.youtube.com/watch?v=BVn1oQL9sWg&amp;t=5">Space Jail</a>!"</p>
# MAGIC <p>Not wanting to be sent to Space Jail, you radio back to the Elves on Earth for help. Although it takes almost three hours for their reply signal to reach you, they send instructions for how to power up the <em>emergency hull painting robot</em> and even provide a small <a href="9">Intcode program</a> (your puzzle input) that will cause it to paint your ship appropriately.</p>
# MAGIC <p>There's just one problem: you don't have an emergency hull painting robot.</p>
# MAGIC <p>You'll need to build a new emergency hull painting robot. The robot needs to be able to move around on the grid of square panels on the side of your ship, detect the color of its current panel, and paint its current panel <em>black</em> or <em>white</em>. (All of the panels are currently <em>black</em>.)</p>
# MAGIC <p>The Intcode program will serve as the brain of the robot. The program uses input instructions to access the robot's camera: provide <code>0</code> if the robot is over a <em>black</em> panel or <code>1</code> if the robot is over a <em>white</em> panel. Then, the program will output two values:</p>
# MAGIC <ul>
# MAGIC <li>First, it will output a value indicating the <em>color to paint the panel</em> the robot is over: <code>0</code> means to paint the panel <em>black</em>, and <code>1</code> means to paint the panel <em>white</em>.</li>
# MAGIC <li>Second, it will output a value indicating the <em>direction the robot should turn</em>: <code>0</code> means it should turn <em>left 90 degrees</em>, and <code>1</code> means it should turn <em>right 90 degrees</em>.</li>
# MAGIC </ul>
# MAGIC <p>After the robot turns, it should always move <em>forward exactly one panel</em>. The robot starts facing <em>up</em>.</p>
# MAGIC <p>The robot will continue running for a while like this and halt when it is finished drawing.  Do not restart the Intcode computer inside the robot during this process.</p>
# MAGIC <p>For example, suppose the robot is about to start running.  Drawing black panels as <code>.</code>, white panels as <code>#</code>, and the robot pointing the direction it is facing (<code>&lt; ^ &gt; v</code>), the initial state and region near the robot looks like this:</p>
# MAGIC <pre><code>.....
# MAGIC .....
# MAGIC ..^..
# MAGIC .....
# MAGIC .....
# MAGIC </code></pre>
# MAGIC <p>The panel under the robot (not visible here because a <code>^</code> is shown instead) is also black, and so any input instructions at this point should be provided <code>0</code>. Suppose the robot eventually outputs <code>1</code> (paint white) and then <code>0</code> (turn left). After taking these actions and moving forward one panel, the region now looks like this:</p>
# MAGIC <pre><code>.....
# MAGIC .....
# MAGIC .&lt;#..
# MAGIC .....
# MAGIC .....
# MAGIC </code></pre>
# MAGIC <p>Input instructions should still be provided <code>0</code>. Next, the robot might output <code>0</code> (paint black) and then <code>0</code> (turn left):</p>
# MAGIC <pre><code>.....
# MAGIC .....
# MAGIC ..#..
# MAGIC .v...
# MAGIC .....
# MAGIC </code></pre>
# MAGIC <p>After more outputs (<code>1,0</code>, <code>1,0</code>):</p>
# MAGIC <pre><code>.....
# MAGIC .....
# MAGIC ..^..
# MAGIC .##..
# MAGIC .....
# MAGIC </code></pre>
# MAGIC <p>The robot is now back where it started, but because it is now on a white panel, input instructions should be provided <code>1</code>.  After several more outputs (<code>0,1</code>, <code>1,0</code>, <code>1,0</code>), the area looks like this:</p>
# MAGIC <pre><code>.....
# MAGIC ..&lt;#.
# MAGIC ...#.
# MAGIC .##..
# MAGIC .....
# MAGIC </code></pre>
# MAGIC <p>Before you deploy the robot, you should probably have an estimate of the area it will cover: specifically, you need to know the <em>number of panels it paints at least once</em>, regardless of color. In the example above, the robot painted <em><code>6</code> panels</em> at least once. (It painted its starting panel twice, but that panel is <a href="https://www.youtube.com/watch?v=KjsSvjA5TuE">still only counted once</a>; it also never painted the panel it ended on.)</p>
# MAGIC <p>Build a new emergency hull painting robot and run the Intcode program on it. <em>How many panels does it paint at least once?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '3,8,1005,8,358,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,29,1,1104,7,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,54,1,103,17,10,1,7,3,10,2,8,9,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,89,1,1009,16,10,1006,0,86,1006,0,89,1006,0,35,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,102,1,8,124,1,105,8,10,1,2,0,10,1,1106,5,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,158,1,102,2,10,1,109,17,10,1,109,6,10,1,1003,1,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,195,1006,0,49,1,101,5,10,1006,0,5,1,108,6,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,232,2,1102,9,10,1,1108,9,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,262,1006,0,47,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,101,0,8,286,1006,0,79,2,1003,2,10,2,107,0,10,1006,0,89,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,323,1006,0,51,2,5,1,10,1,6,15,10,2,1102,3,10,101,1,9,9,1007,9,905,10,1005,10,15,99,109,680,104,0,104,1,21101,838211572492,0,1,21101,0,375,0,1106,0,479,21102,1,48063328668,1,21102,386,1,0,1106,0,479,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,1,21679533248,1,21101,0,433,0,1105,1,479,21102,235190455527,1,1,21102,444,1,0,1106,0,479,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,837901247244,1,21102,1,467,0,1106,0,479,21101,0,709488169828,1,21102,1,478,0,1105,1,479,99,109,2,22102,1,-1,1,21102,1,40,2,21101,0,510,3,21102,1,500,0,1105,1,543,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,505,506,521,4,0,1001,505,1,505,108,4,505,10,1006,10,537,1102,1,0,505,109,-2,2106,0,0,0,109,4,2101,0,-1,542,1207,-3,0,10,1006,10,560,21101,0,0,-3,21201,-3,0,1,21202,-2,1,2,21102,1,1,3,21102,1,579,0,1105,1,584,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,607,2207,-4,-2,10,1006,10,607,21202,-4,1,-4,1106,0,675,21202,-4,1,1,21201,-3,-1,2,21202,-2,2,3,21101,0,626,0,1106,0,584,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,645,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,667,22101,0,-1,1,21102,1,667,0,105,1,542,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0'

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

def get_panels(computer):
  turn = {
    'up': ['left', 'right'],
    'right': ['up', 'down'],
    'down': ['right', 'left'],
    'left': ['down', 'up']
  }
  panels = collections.defaultdict(int)

  x, y = 0, 0
  heading = 'up'
  while computer.run().state != State.HALTED:
    paint, direction = computer.output_values
    computer.output_values.clear()

    panels[(x, y)] = paint

    heading = turn[heading][direction]
    x += (heading == 'right') - (heading == 'left')
    y += (heading == 'down') - (heading == 'up')

    computer.input_values.append(panels[(x, y)])
  return panels
  
instructions = collections.defaultdict(int, {i: int(x) for i, x in enumerate(inp.split(','))})

answer = len(get_panels(Computer(instructions, [0])))
print(answer)

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You're not sure what it's trying to paint, but it's definitely not a <em>registration identifier</em>.  The Space Police are getting impatient.</p>
# MAGIC <p>Checking your external ship cameras again, you notice a white panel marked "emergency hull painting robot starting panel". The rest of the panels are <em>still black</em>, but it looks like the robot was expecting to <em>start on a white panel</em>, not a black one.</p>
# MAGIC <p>Based on the <span title="Just be glad it wasn't a full set of Space Law Space Books; the number of pages is *astronomical*.">Space Law Space Brochure</span> that the Space Police attached to one of your windows, a valid registration identifier is always <em>eight capital letters</em>. After starting the robot on a single <em>white panel</em> instead, <em>what registration identifier does it paint</em> on your hull?</p>
# MAGIC </article>

# COMMAND ----------

panels = get_panels(Computer(instructions, [1]))
x_max, y_max = (max(dimension) for dimension in zip(*panels))
for y in range(y_max + 1):
  print()
  for x in range(x_max + 1):
    print('#' if panels[(x, y)] else ' ', end='')

# COMMAND ----------

answer = 'HGEHJHUZ'
print(answer)
