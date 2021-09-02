# Databricks notebook source
# MAGIC %md https://adventofcode.com/2015/day/23

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2>--- Day 23: Opening the Turing Lock ---</h2><p>Little Jane Marie just got her very first computer for Christmas from some <span title="Definitely not Wintermute.">unknown benefactor</span>.  It comes with instructions and an example program, but the computer itself seems to be malfunctioning.  She's curious what the program does, and would like you to help her run it.</p>
# MAGIC <p>The manual explains that the computer supports two <a href="https://en.wikipedia.org/wiki/Processor_register">registers</a> and six <a href="https://en.wikipedia.org/wiki/Instruction_set">instructions</a> (truly, it goes on to remind the reader, a state-of-the-art technology). The registers are named <code>a</code> and <code>b</code>, can hold any <a href="https://en.wikipedia.org/wiki/Natural_number">non-negative integer</a>, and begin with a value of <code>0</code>.  The instructions are as follows:</p>
# MAGIC <ul>
# MAGIC <li><code>hlf r</code> sets register <code>r</code> to <em>half</em> its current value, then continues with the next instruction.</li>
# MAGIC <li><code>tpl r</code> sets register <code>r</code> to <em>triple</em> its current value, then continues with the next instruction.</li>
# MAGIC <li><code>inc r</code> <em>increments</em> register <code>r</code>, adding <code>1</code> to it, then continues with the next instruction.</li>
# MAGIC <li><code>jmp offset</code> is a <em>jump</em>; it continues with the instruction <code>offset</code> away <em>relative to itself</em>.</li>
# MAGIC <li><code>jie r, offset</code> is like <code>jmp</code>, but only jumps if register <code>r</code> is <em>even</em> ("jump if even").</li>
# MAGIC <li><code>jio r, offset</code> is like <code>jmp</code>, but only jumps if register <code>r</code> is <code>1</code> ("jump if <em>one</em>", not odd).</li>
# MAGIC </ul>
# MAGIC <p>All three jump instructions work with an <em>offset</em> relative to that instruction.  The offset is always written with a prefix <code>+</code> or <code>-</code> to indicate the direction of the jump (forward or backward, respectively).  For example, <code>jmp +1</code> would simply continue with the next instruction, while <code>jmp +0</code> would continuously jump back to itself forever.</p>
# MAGIC <p>The program exits when it tries to run an instruction beyond the ones defined.</p>
# MAGIC <p>For example, this program sets <code>a</code> to <code>2</code>, because the <code>jio</code> instruction causes it to skip the <code>tpl</code> instruction:</p>
# MAGIC <pre><code>inc a
# MAGIC jio a, +2
# MAGIC tpl a
# MAGIC inc a
# MAGIC </code></pre>
# MAGIC <p>What is <em>the value in register <code>b</code></em> when the program in your puzzle input is finished executing?</p>
# MAGIC </article>

# COMMAND ----------

inp = '''jio a, +16
inc a
inc a
tpl a
tpl a
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
tpl a
inc a
jmp +23
tpl a
inc a
inc a
tpl a
inc a
inc a
tpl a
tpl a
inc a
inc a
tpl a
inc a
tpl a
inc a
tpl a
inc a
inc a
tpl a
inc a
tpl a
tpl a
inc a
jio a, +8
inc b
jie a, +4
tpl a
inc a
jmp +2
hlf a
jmp -7'''

# COMMAND ----------

import re

instructions = [re.findall(r'[^, ]+', line) for line in inp.split('\n')]

# COMMAND ----------

def run_instructions(instructions, registers):
  i = 0
  while i < len(instructions):
    instruction, *args = instructions[i]
    
    if instruction == 'hlf':
      registers[args[0]] = registers[args[0]] / 2
    elif instruction == 'tpl':
      registers[args[0]] = registers[args[0]] * 3
    elif instruction == 'inc':
      registers[args[0]] += 1
    elif instruction == 'jmp':
      i += int(args[0]) - 1
    elif instruction == 'jie':
      if registers[args[0]] % 2 == 0:
        i += int(args[1]) - 1
    elif instruction == 'jio':
      if registers[args[0]] == 1:
        i += int(args[1]) - 1
    
    i += 1
    

registers = {'a': 0, 'b': 0}
run_instructions(instructions, registers)
answer = registers['b']
answer

# COMMAND ----------

# MAGIC %md <article class="day-desc"><h2 id="part2">--- Part Two ---</h2><p>The unknown benefactor is <em>very</em> thankful for releasi-- er, helping little Jane Marie with her computer.  Definitely not to distract you, what is the value in register <code>b</code> after the program is finished executing if register <code>a</code> starts as <code>1</code> instead?</p>
# MAGIC </article>

# COMMAND ----------

registers = {'a': 1, 'b': 0}
run_instructions(instructions, registers)
answer = registers['b']
answer
