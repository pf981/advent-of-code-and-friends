# Databricks notebook source
# MAGIC %md https://adventofcode.com/2019/day/15

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 15: Oxygen System ---</h2><p>Out here in deep space, many things can go wrong. Fortunately, many of those things have <span title="Which indicator lights indicate when the indicator lights have failed?">indicator lights</span>. Unfortunately, one of those lights is lit: the oxygen system for part of the ship has failed!</p>
# MAGIC <p>According to the readouts, the oxygen system must have failed days ago after a rupture in oxygen tank two; that section of the ship was automatically sealed once oxygen levels went dangerously low. A single remotely-operated <em>repair droid</em> is your only option for fixing the oxygen system.</p>
# MAGIC <p>The Elves' care package included an <a href="9">Intcode</a> program (your puzzle input) that you can use to remotely control the repair droid. By running that program, you can direct the repair droid to the oxygen system and fix the problem.</p>
# MAGIC <p>The remote control program executes the following steps in a loop forever:</p>
# MAGIC <ul>
# MAGIC <li>Accept a <em>movement command</em> via an input instruction.</li>
# MAGIC <li>Send the movement command to the repair droid.</li>
# MAGIC <li>Wait for the repair droid to finish the movement operation.</li>
# MAGIC <li>Report on the <em>status</em> of the repair droid via an output instruction.</li>
# MAGIC </ul>
# MAGIC <p>Only four <em>movement commands</em> are understood: north (<code>1</code>), south (<code>2</code>), west (<code>3</code>), and east (<code>4</code>). Any other command is invalid. The movements differ in direction, but not in distance: in a long enough east-west hallway, a series of commands like <code>4,4,4,4,3,3,3,3</code> would leave the repair droid back where it started.</p>
# MAGIC <p>The repair droid can reply with any of the following <em>status</em> codes:</p>
# MAGIC <ul>
# MAGIC <li><code>0</code>: The repair droid hit a wall. Its position has not changed.</li>
# MAGIC <li><code>1</code>: The repair droid has moved one step in the requested direction.</li>
# MAGIC <li><code>2</code>: The repair droid has moved one step in the requested direction; its new position is the location of the oxygen system.</li>
# MAGIC </ul>
# MAGIC <p>You don't know anything about the area around the repair droid, but you can figure it out by watching the status codes.</p>
# MAGIC <p>For example, we can draw the area using <code>D</code> for the droid, <code>#</code> for walls, <code>.</code> for locations the droid can traverse, and empty space for unexplored locations.  Then, the initial state looks like this:</p>
# MAGIC <pre><code>      
# MAGIC       
# MAGIC    D  
# MAGIC       
# MAGIC       
# MAGIC </code></pre>
# MAGIC <p>To make the droid go north, send it <code>1</code>. If it replies with <code>0</code>, you know that location is a wall and that the droid didn't move:</p>
# MAGIC <pre><code>      
# MAGIC    #  
# MAGIC    D  
# MAGIC       
# MAGIC       
# MAGIC </code></pre>
# MAGIC <p>To move east, send <code>4</code>; a reply of <code>1</code> means the movement was successful:</p>
# MAGIC <pre><code>      
# MAGIC    #  
# MAGIC    .D 
# MAGIC       
# MAGIC       
# MAGIC </code></pre>
# MAGIC <p>Then, perhaps attempts to move north (<code>1</code>), south (<code>2</code>), and east (<code>4</code>) are all met with replies of <code>0</code>:</p>
# MAGIC <pre><code>      
# MAGIC    ## 
# MAGIC    .D#
# MAGIC     # 
# MAGIC       
# MAGIC </code></pre>
# MAGIC <p>Now, you know the repair droid is in a dead end. Backtrack with <code>3</code> (which you already know will get a reply of <code>1</code> because you already know that location is open):</p>
# MAGIC <pre><code>      
# MAGIC    ## 
# MAGIC    D.#
# MAGIC     # 
# MAGIC       
# MAGIC </code></pre>
# MAGIC <p>Then, perhaps west (<code>3</code>) gets a reply of <code>0</code>, south (<code>2</code>) gets a reply of <code>1</code>, south again (<code>2</code>) gets a reply of <code>0</code>, and then west (<code>3</code>) gets a reply of <code>2</code>:</p>
# MAGIC <pre><code>      
# MAGIC    ## 
# MAGIC   #..#
# MAGIC   D.# 
# MAGIC    #  
# MAGIC </code></pre>
# MAGIC <p>Now, because of the reply of <code>2</code>, you know you've found the <em>oxygen system</em>! In this example, it was only <code><em>2</em></code> moves away from the repair droid's starting position.</p>
# MAGIC <p><em>What is the fewest number of movement commands</em> required to move the repair droid from its starting position to the location of the oxygen system?</p>
# MAGIC </article>

# COMMAND ----------

inp = '3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,1002,1034,1,1039,102,1,1036,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1106,0,124,1001,1034,0,1039,102,1,1036,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1105,1,124,1001,1034,-1,1039,1008,1036,0,1041,1002,1035,1,1040,101,0,1038,1043,1002,1037,1,1042,1106,0,124,1001,1034,1,1039,1008,1036,0,1041,1001,1035,0,1040,1002,1038,1,1043,1002,1037,1,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,35,1032,1006,1032,165,1008,1040,7,1032,1006,1032,165,1101,2,0,1044,1105,1,224,2,1041,1043,1032,1006,1032,179,1101,1,0,1044,1105,1,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,38,1044,1106,0,224,1101,0,0,1044,1105,1,224,1006,1044,247,1001,1039,0,1034,101,0,1040,1035,101,0,1041,1036,102,1,1043,1038,102,1,1042,1037,4,1044,1106,0,0,4,23,34,36,20,5,93,36,72,13,75,47,14,34,44,15,61,24,50,12,76,22,40,17,13,24,59,32,99,35,33,5,31,91,44,27,11,21,15,20,99,6,62,16,62,6,14,69,10,53,37,52,99,18,92,33,19,99,6,82,13,19,45,15,21,39,59,1,24,39,79,77,35,5,69,79,95,28,49,71,7,83,81,99,58,17,3,98,37,11,14,29,44,50,23,75,1,15,67,45,35,44,93,62,31,6,85,81,24,19,22,86,54,19,77,6,4,15,35,40,42,7,9,69,2,53,63,78,94,29,82,3,16,64,86,48,36,57,20,54,25,7,89,51,31,52,17,64,51,12,67,6,99,12,17,99,10,73,16,25,57,78,2,4,46,37,96,25,9,96,80,6,60,9,7,3,24,52,33,73,23,22,71,24,77,19,96,35,86,50,93,2,75,25,59,14,79,31,54,4,24,87,17,18,88,25,36,49,87,22,22,20,76,31,62,18,39,39,35,70,79,37,35,72,26,25,96,8,35,25,60,26,34,5,21,37,79,65,99,50,7,33,54,69,39,35,21,72,9,67,16,92,47,65,89,20,77,34,85,24,87,3,49,62,2,81,17,49,31,41,29,80,18,63,2,70,18,96,31,53,70,24,37,78,59,20,74,8,67,93,29,24,71,19,23,28,90,10,21,34,49,18,14,48,90,13,54,93,4,96,95,23,26,85,3,3,99,24,43,8,72,19,50,17,58,94,5,50,16,12,91,25,68,68,42,27,54,49,2,44,47,31,3,35,66,36,67,2,84,74,14,3,5,63,95,21,23,47,22,61,25,28,69,3,50,13,74,96,53,9,32,21,90,8,8,34,66,49,18,34,63,28,90,37,14,43,33,97,12,39,96,31,23,76,14,16,12,74,43,10,63,14,20,95,73,1,59,5,40,97,42,47,29,54,64,17,73,44,10,44,43,42,53,37,37,29,48,9,10,18,28,69,62,25,50,53,29,15,60,10,74,1,83,21,21,49,19,61,35,30,99,87,10,42,17,4,67,87,6,89,2,21,56,1,80,24,1,64,24,42,95,20,95,77,23,29,84,39,5,91,65,16,39,46,36,57,23,30,49,70,21,7,92,22,90,1,25,41,20,35,59,54,98,88,40,23,33,99,5,95,28,73,15,72,76,8,2,11,86,23,31,6,69,13,23,93,86,59,24,16,90,23,32,41,11,50,84,58,28,40,3,71,12,86,33,45,34,33,81,23,10,33,53,28,81,68,15,96,4,68,3,54,19,73,27,3,21,99,5,47,77,26,28,49,35,92,4,18,1,66,16,1,28,28,66,56,26,23,45,53,20,55,32,26,57,67,5,86,73,9,70,2,87,16,75,93,31,78,66,14,76,4,64,24,80,20,45,15,75,17,54,85,16,16,28,45,20,85,34,7,2,82,59,25,15,58,92,36,88,46,22,78,6,71,15,23,67,14,71,60,33,56,10,61,7,40,79,37,59,58,37,34,59,17,80,10,90,11,89,95,9,37,9,45,60,10,29,73,4,95,42,29,54,49,21,36,65,34,21,94,70,37,86,33,92,84,15,18,72,82,28,12,12,25,91,40,68,2,8,83,59,62,4,29,75,79,34,21,99,24,90,79,13,22,92,62,73,19,9,84,46,11,88,32,92,35,58,79,31,4,30,90,21,93,14,76,55,48,23,43,13,89,13,67,33,90,86,70,32,65,15,77,32,48,25,61,27,58,2,81,36,59,10,77,5,95,35,41,50,88,0,0,21,21,1,10,1,0,0,0,0,0,0'

# COMMAND ----------

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

# COMMAND ----------

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

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>You quickly repair the oxygen system; oxygen gradually fills the area.</p>
# MAGIC <p>Oxygen starts in the location containing the repaired oxygen system. It takes <em>one minute</em> for oxygen to spread to all open locations that are adjacent to a location that already contains oxygen. Diagonal locations are <em>not</em> adjacent.</p>
# MAGIC <p>In the example above, suppose you've used the droid to explore the area fully and have the following map (where locations that currently contain oxygen are marked <code>O</code>):</p>
# MAGIC <pre><code> ##   
# MAGIC #..## 
# MAGIC #.#..#
# MAGIC #.O.# 
# MAGIC  ###  
# MAGIC </code></pre>
# MAGIC <p>Initially, the only location which contains oxygen is the location of the repaired oxygen system.  However, after one minute, the oxygen spreads to all open (<code>.</code>) locations that are adjacent to a location containing oxygen:</p>
# MAGIC <pre><code> ##   
# MAGIC #..## 
# MAGIC #.#..#
# MAGIC #OOO# 
# MAGIC  ###  
# MAGIC </code></pre>
# MAGIC <p>After a total of two minutes, the map looks like this:</p>
# MAGIC <pre><code> ##   
# MAGIC #..## 
# MAGIC #O#O.#
# MAGIC #OOO# 
# MAGIC  ###  
# MAGIC </code></pre>
# MAGIC <p>After a total of three minutes:</p>
# MAGIC <pre><code> ##   
# MAGIC #O.## 
# MAGIC #O#OO#
# MAGIC #OOO# 
# MAGIC  ###  
# MAGIC </code></pre>
# MAGIC <p>And finally, the whole region is full of oxygen after a total of four minutes:</p>
# MAGIC <pre><code> ##   
# MAGIC #OO## 
# MAGIC #O#OO#
# MAGIC #OOO# 
# MAGIC  ###  
# MAGIC </code></pre>
# MAGIC <p>So, in this example, all locations contain oxygen after <code><em>4</em></code> minutes.</p>
# MAGIC <p>Use the repair droid to get a complete map of the area. <em>How many minutes will it take to fill with oxygen?</em></p>
# MAGIC </article>

# COMMAND ----------

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
