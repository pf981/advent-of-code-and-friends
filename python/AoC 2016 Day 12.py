# Databricks notebook source
# MAGIC %md https://adventofcode.com/2016/day/12

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 12: Leonardo's Monorail ---</h2><p>You finally reach the top floor of this building: a garden with a slanted glass ceiling. Looks like there are no more stars to be had.</p>
# MAGIC <p>While sitting on a nearby bench amidst some <a href="https://www.google.com/search?q=tiger+lilies&amp;tbm=isch">tiger lilies</a>, you manage to decrypt some of the files you extracted from the servers downstairs.</p>
# MAGIC <p>According to these documents, Easter Bunny HQ isn't just this building - it's a collection of buildings in the nearby area. They're all connected by a local monorail, and there's another building not far from here! Unfortunately, being night, the monorail is currently not operating.</p>
# MAGIC <p>You remotely connect to the monorail control systems and discover that the boot sequence expects a password. The password-checking logic (your puzzle input) is easy to extract, but the code it uses is strange: it's <span title="Strangely, this assembunny code doesn't seem to be very good at multiplying.">assembunny</span> code designed for the <a href="11">new computer</a> you just assembled. You'll have to execute the code and get the password.</p>
# MAGIC <p>The assembunny code you've extracted operates on four <a href="https://en.wikipedia.org/wiki/Processor_register">registers</a> (<code>a</code>, <code>b</code>, <code>c</code>, and <code>d</code>) that start at <code>0</code> and can hold any <a href="https://en.wikipedia.org/wiki/Integer">integer</a>. However, it seems to make use of only a few <a href="https://en.wikipedia.org/wiki/Instruction_set">instructions</a>:</p>
# MAGIC <ul>
# MAGIC <li><code>cpy x y</code> <em>copies</em> <code>x</code> (either an integer or the <em>value</em> of a register) into register <code>y</code>.</li>
# MAGIC <li><code>inc x</code> <em>increases</em> the value of register <code>x</code> by one.</li>
# MAGIC <li><code>dec x</code> <em>decreases</em> the value of register <code>x</code> by one.</li>
# MAGIC <li><code>jnz x y</code> <em>jumps</em> to an instruction <code>y</code> away (positive means forward; negative means backward), but only if <code>x</code> is <em>not zero</em>.</li>
# MAGIC </ul>
# MAGIC <p>The <code>jnz</code> instruction moves relative to itself: an offset of <code>-1</code> would continue at the previous instruction, while an offset of <code>2</code> would <em>skip over</em> the next instruction.</p>
# MAGIC <p>For example:</p>
# MAGIC <pre><code>cpy 41 a
# MAGIC inc a
# MAGIC inc a
# MAGIC dec a
# MAGIC jnz a 2
# MAGIC dec a
# MAGIC </code></pre>
# MAGIC <p>The above code would set register <code>a</code> to <code>41</code>, increase its value by <code>2</code>, decrease its value by <code>1</code>, and then skip the last <code>dec a</code> (because <code>a</code> is not zero, so the <code>jnz a 2</code> skips it), leaving register <code>a</code> at <code>42</code>. When you move past the last instruction, the program halts.</p>
# MAGIC <p>After executing the assembunny code in your puzzle input, <em>what value is left in register <code>a</code>?</em></p>
# MAGIC </article>

# COMMAND ----------

inp = '''cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 13 c
cpy 14 d
inc a
dec d
jnz d -2
dec c
jnz c -5'''

# COMMAND ----------

from collections import defaultdict
from dataclasses import dataclass, field
from typing import DefaultDict

@dataclass
class Computer:
  instructions: dict
  registers: DefaultDict[str, int] = field(default_factory=lambda: defaultdict(int))
  line_number: int = 0
  status: str = 'Pending'
    
  def __post_init__(self):
    self.instructions = self.instructions.copy()
    
  def _get_value(self, x):
    try:
      return int(x)
    except ValueError:
      return self.registers[x]
  
  def run_once(self):
    instruction, args = self.instructions[self.line_number]
    
    if instruction == 'cpy':
      self.registers[args[1]] = self._get_value(args[0])
    elif instruction == 'inc':
      self.registers[args[0]] += 1
    elif instruction == 'dec':
      self.registers[args[0]] -= 1
    elif instruction == 'jnz':
      if self._get_value(args[0]) != 0:
        self.line_number += self._get_value(args[1]) - 1
    
    self.line_number += 1
    if self.line_number >= len(self.instructions):
      self.status = 'Halted'
  
  def run(self):
    while self.status != 'Halted':
      self.run_once()


instructions = {i: (line.split()[0], tuple(line.split()[1:])) for i, line in enumerate(inp.split('\n'))}

computer = Computer(instructions)
computer.run()

answer = computer.registers['a']
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>As you head down the fire escape to the monorail, you notice it didn't start; register <code>c</code> needs to be initialized to the position of the ignition key.</p>
# MAGIC <p>If you instead <em>initialize register <code>c</code> to be <code>1</code></em>, what value is now left in register <code>a</code>?</p>
# MAGIC </article>

# COMMAND ----------

computer = Computer(instructions)
computer.registers['c'] = 1
computer.run()

answer = computer.registers['a']
answer
