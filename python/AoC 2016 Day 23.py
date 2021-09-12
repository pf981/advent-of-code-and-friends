# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/23

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 23: Safe Cracking ---</h2><p>This is one of the top floors of the nicest tower in EBHQ. The Easter Bunny's private office is here, complete with a safe hidden behind a painting, and who <em>wouldn't</em> hide a star in a safe behind a painting?</p>
# MAGIC <p>The safe has a digital screen and keypad for code entry. A sticky note attached to the safe has a password hint on it: "eggs". The painting is of a large rabbit coloring some eggs. You see <code>7</code>.</p>
# MAGIC <p>When you go to type the code, though, nothing appears on the display; instead, the keypad comes apart in your hands, apparently having been smashed. Behind it is some kind of socket - one that matches a connector in your <a href="11">prototype computer</a>! You pull apart the smashed keypad and extract the logic circuit, plug it into your computer, and plug your computer into the safe.</p>
# MAGIC <p></p>Now, you just need to figure out what output the keypad would have sent to the safe. You extract the <a href="12">assembunny code</a> from the logic chip (your puzzle input).<p></p>
# MAGIC <p>The code looks like it uses <em>almost</em> the same architecture and instruction set that the <a href="12">monorail computer</a> used! You should be able to <em>use the same assembunny interpreter</em> for this as you did there, but with one new instruction:</p>
# MAGIC <p><code>tgl x</code> <em>toggles</em> the instruction <code>x</code> away (pointing at instructions like <code>jnz</code> does: positive means forward; negative means backward):</p>
# MAGIC <ul>
# MAGIC <li>For <em>one-argument</em> instructions, <code>inc</code> becomes <code>dec</code>, and all other one-argument instructions become <code>inc</code>.</li>
# MAGIC <li>For <em>two-argument</em> instructions, <code>jnz</code> becomes <code>cpy</code>, and all other two-instructions become <code>jnz</code>.</li>
# MAGIC <li>The arguments of a toggled instruction are <em>not affected</em>.</li>
# MAGIC <li>If an attempt is made to toggle an instruction outside the program, <em>nothing happens</em>.</li>
# MAGIC <li>If toggling produces an <em>invalid instruction</em> (like <code>cpy 1 2</code>) and an attempt is later made to execute that instruction, <em>skip it instead</em>.</li>
# MAGIC <li>If <code>tgl</code> toggles <em>itself</em> (for example, if <code>a</code> is <code>0</code>, <code>tgl a</code> would target itself and become <code>inc a</code>), the resulting instruction is not executed until the next time it is reached.</li>
# MAGIC </ul>
# MAGIC <p>For example, given this program:</p>
# MAGIC <pre><code>cpy 2 a
# MAGIC tgl a
# MAGIC tgl a
# MAGIC tgl a
# MAGIC cpy 1 a
# MAGIC dec a
# MAGIC dec a
# MAGIC </code></pre>
# MAGIC <ul>
# MAGIC <li><code>cpy 2 a</code> initializes register <code>a</code> to <code>2</code>.</li>
# MAGIC <li>The first <code>tgl a</code> toggles an instruction <code>a</code> (<code>2</code>) away from it, which changes the third <code>tgl a</code> into <code>inc a</code>.</li>
# MAGIC <li>The second <code>tgl a</code> also modifies an instruction <code>2</code> away from it, which changes the <code>cpy 1 a</code> into <code>jnz 1 a</code>.</li>
# MAGIC <li>The fourth line, which is now <code>inc a</code>, increments <code>a</code> to <code>3</code>.</li>
# MAGIC <li>Finally, the fifth line, which is now <code>jnz 1 a</code>, jumps <code>a</code> (<code>3</code>) instructions ahead, skipping the <code>dec a</code> instructions.</li>
# MAGIC </ul>
# MAGIC <p>In this example, the final value in register <code>a</code> is <code>3</code>.</p>
# MAGIC <p>The rest of the electronics seem to place the keypad entry (the number of eggs, <code>7</code>) in register <code>a</code>, run the code, and then send the value left in register <code>a</code> to the safe.</p>
# MAGIC <p><em>What value</em> should be sent to the safe?</p>
# MAGIC </article>

# COMMAND ----------

inp = '''cpy a b
dec b
cpy a d
cpy 0 a
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
tgl c
cpy -16 c
jnz 1 c
cpy 95 c
jnz 99 d
inc a
inc d
jnz d -2
inc c
jnz c -5'''

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
    
    if instruction == 'cpy':
      try:
        int(args[1])
      except ValueError:
        self.registers[args[1]] = self._get_value(args[0])
    elif instruction == 'inc':
      self.registers[args[0]] += 1
    elif instruction == 'dec':
      self.registers[args[0]] -= 1
    elif instruction == 'jnz':
      if self._get_value(args[0]) != 0:
        self.line_number += self._get_value(args[1]) - 1
    elif instruction == 'tgl':
      target_line = self.line_number + self._get_value(args[0])
      if target_line < len(self.instructions):
        self.instructions[target_line][0] = {
          'cpy': 'jnz',
          'inc': 'dec',
          'dec': 'inc',
          'jnz': 'cpy',
          'tgl': 'inc'
        }[self.instructions[target_line][0]]
    elif instruction == 'mul':
      self.registers[args[2]] = self._get_value(args[0]) * self._get_value(args[1])
    elif instruction == 'nop':
      pass
    else:
      raise ValueError(f'Unknown instruction: {instruction}')
    
    self.line_number += 1
    if self.line_number >= len(self.instructions):
      self.status = 'Halted'
  
  def run(self):
    while self.status != 'Halted':
      self.run_once()


instructions = {i: [line.split()[0], tuple(line.split()[1:])] for i, line in enumerate(inp.split('\n'))}

computer = Computer(instructions)
computer.registers['a'] = 7
computer.run()

answer = computer.registers['a']
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The safe doesn't open, but it <em>does</em> make several <span title="SUCH INCORRECT! VERY LOCK! WOW!">angry noises</span> to express its frustration.</p>
# MAGIC <p>You're quite sure your logic is working correctly, so the only other thing is... you check the painting again. As it turns out, colored eggs are still eggs. Now you count <code>12</code>.</p>
# MAGIC <p>As you run the program with this new input, the prototype computer begins to <em>overheat</em>. You wonder what's taking so long, and whether the lack of any instruction more powerful than "add one" has anything to do with it. Don't bunnies usually <em>multiply</em>?</p>
# MAGIC <p>Anyway, <em>what value</em> should actually be sent to the safe?</p>
# MAGIC </article>

# COMMAND ----------

# Label |  Line  |  Instruction  |    V1                |    V2                            |  V3
# -----------------------------------------------------------------------------------------|-------------
#       |  0     |  cpy a b      |    b = a             |                                  |             
#       |  1     |  dec b        |    b--               |                                  |             
# D:    |  2     |  cpy a d      |    d = a             |                                  |             
#       |  3     |  cpy 0 a      |    a = 0             |                                  |             
# B:    |  4     |  cpy b c      |    c = b             |  WHILE d > 0 { c = b             |  a = d * b  
# A:    |  5     |  inc a        |    a++               |                WHILE C > 0 { a++ |  ;          
#       |  6     |  dec c        |    c--               |                              c-- |  ;          
#       |  7     |  jnz c -2     |    IF c != 0 GOTO A  |                }                 |  ;          
#       |  8     |  dec d        |    d--               |                d--               |  ;          
#       |  9     |  jnz d -5     |    if d != 0 GOTO B  |              }                   |  ;          
#       |  10    |  dec b        |    b--               |  b--                             |  b--        
#       |  11    |  cpy b c      |    c = b             |                                  |             
#       |  12    |  cpy c d      |    d = c             |                                  |             
# C:    |  13    |  dec d        |    d--               |                                  |             
#       |  14    |  inc c        |    c++               |                                  |             
#       |  15    |  jnz d -2     |    if d != 0 GOTO C  |                                  |             
#       |  16    |  tgl c        |    ???               |                                  |             
#       |  17    |  cpy -16 c    |    c = -16           |                                  |             
#       |  18    |  jnz 1 c      |    GOTO D            |                                  |             
#       |  19    |  cpy 95 c     |    c = 95            |                                  |             
# F:    |  20    |  jnz 99 d     |    GOTO d ???        |                                  |             
# E:    |  21    |  inc a        |    a--               |                                  |             
#       |  22    |  inc d        |    d--               |                                  |             
#       |  23    |  jnz d -2     |    IF d != 0 GOTO E  |                                  |             
#       |  24    |  inc c        |    c++               |                                  |             
#       |  25    |  jnz c -5     |    IF c != 0 GOTO F  |                                  |               

# COMMAND ----------

instructions[4] = ['mul', ('d', 'b', 'a')]
for i in range(5, 10):
  instructions[i] = ['nop', tuple()]

computer = Computer(instructions)
computer.registers['a'] = 12
computer.run()

answer = computer.registers['a']
answer
