# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/25

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 25: Clock Signal ---</h2><p>You open the door and find yourself on the roof. The city sprawls away from you for miles and miles.</p>
# MAGIC <p>There's not much time now - it's already Christmas, but you're nowhere near the North Pole, much too far to deliver these stars to the sleigh in time.</p>
# MAGIC <p>However, maybe the <em>huge antenna</em> up here can offer a solution. After all, the sleigh doesn't need the stars, exactly; it needs the timing data they provide, and you happen to have a massive signal generator right here.</p>
# MAGIC <p>You connect the stars you have to your prototype computer, connect that to the antenna, and begin the transmission.</p>
# MAGIC <p><span title="Then again, if something ever works on the first try, you should be *very* suspicious.">Nothing happens.</span></p>
# MAGIC <p>You call the service number printed on the side of the antenna and quickly explain the situation. "I'm not sure what kind of equipment you have connected over there," he says, "but you need a clock signal." You try to explain that this is a signal for a clock.</p>
# MAGIC <p>"No, no, a <a href="https://en.wikipedia.org/wiki/Clock_signal">clock signal</a> - timing information so the antenna computer knows how to read the data you're sending it. An endless, alternating pattern of <code>0</code>, <code>1</code>, <code>0</code>, <code>1</code>, <code>0</code>, <code>1</code>, <code>0</code>, <code>1</code>, <code>0</code>, <code>1</code>...." He trails off.</p>
# MAGIC <p>You ask if the antenna can handle a clock signal at the frequency you would need to use for the data from the stars. "There's <em>no way</em> it can! The only antenna we've installed capable of <em>that</em> is on top of a top-secret Easter Bunny installation, and you're <em>definitely</em> not-" You hang up the phone.</p>
# MAGIC <p>You've extracted the antenna's clock signal generation <a href="12">assembunny</a> code (your puzzle input); it looks mostly compatible with code you worked on <a href="23">just recently</a>.</p>
# MAGIC <p>This antenna code, being a signal generator, uses one extra instruction:</p>
# MAGIC <ul>
# MAGIC <li><code>out x</code> <em>transmits</em> <code>x</code> (either an integer or the <em>value</em> of a register) as the next value for the clock signal.</li>
# MAGIC </ul>
# MAGIC <p>The code takes a value (via register <code>a</code>) that describes the signal to generate, but you're not sure how it's used. You'll have to find the input to produce the right signal through experimentation.</p>
# MAGIC <p><em>What is the lowest positive integer</em> that can be used to initialize register <code>a</code> and cause the code to output a clock signal of <code>0</code>, <code>1</code>, <code>0</code>, <code>1</code>... repeating forever?</p>
# MAGIC </article>

# COMMAND ----------

inp = '''cpy a d
cpy 7 c
cpy 362 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy d a
jnz 0 0
cpy a b
cpy 0 a
cpy 2 c
jnz b 2
jnz 1 6
dec b
dec c
jnz c -4
inc a
jnz 1 -7
cpy 2 b
jnz c 2
jnz 1 4
dec b
dec c
jnz 1 -4
jnz 0 0
out b
jnz a -19
jnz 1 -21'''

# COMMAND ----------

from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass, field
from typing import DefaultDict

@dataclass
class Computer:
  instructions: dict
  registers: DefaultDict[str, int] = field(default_factory=lambda: defaultdict(int))
  line_number: int = 0
  status: str = 'Pending'
    
  def __post_init__(self):
    self.instructions = deepcopy(self.instructions)
    
  def _get_value(self, x):
    try:
      return int(x)
    except ValueError:
      return self.registers[x]
  
  def run_once(self):
    instruction, args = self.instructions[self.line_number]
    out = None
    
    if instruction == 'cpy':
      self.registers[args[1]] = self._get_value(args[0])
    elif instruction == 'inc':
      self.registers[args[0]] += 1
    elif instruction == 'dec':
      self.registers[args[0]] -= 1
    elif instruction == 'jnz':
      if self._get_value(args[0]) != 0:
        self.line_number += self._get_value(args[1]) - 1
    elif instruction == 'out':
      out = self._get_value(args[0])
    else:
      raise ValueError(f'Unknown instruction: {instruction}')
    
    self.line_number += 1
    if self.line_number >= len(self.instructions):
      self.status = 'Halted'
    return out
  
  def is_clock(self):
    clock_i = 0
    while clock_i < 100:
      out = self.run_once()
      if self.status == 'Halted':
        return False
      
      if out is not None:
        if clock_i % 2 != out:
          return False
        clock_i += 1
    return True

instructions = {i: (line.split()[0], tuple(line.split()[1:])) for i, line in enumerate(inp.split('\n'))}

# COMMAND ----------

import itertools

for a in itertools.count():
  computer = Computer(instructions)
  computer.registers['a'] = a
  if computer.is_clock():
     break

answer = a
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The antenna is ready. Now, all you need is the <em class="star">fifty stars</em> required to generate the signal for the sleigh, but you don't have enough.</p>
# MAGIC <p>You look toward the sky in desperation... suddenly noticing that a lone star has been installed at the top of the antenna!  Only <em>49 more</em> to go.</p>
# MAGIC </article>

# COMMAND ----------

# No puzzle here - just need 49 stars.
